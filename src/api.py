# This API file will pull multiple school years (e.g., 2017-2018 through 2022-2023)
# and save separate CSVs.

import time
import requests
import pandas as pd

BASE_URL = "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICSCH_{}/MapServer/0/query"


def get_json(session, url, params, timeout=(10, 90), retries=6):
    for attempt in range(1, retries + 1):
        try:
            r = session.get(url, params=params, timeout=timeout)
            r.raise_for_status()
            return r.json()
        except (requests.RequestException, ValueError) as e:
            if attempt == retries:
                raise
            sleep_s = min(60, 2 ** attempt)
            print(f"[retry {attempt}/{retries}] {e} -> sleeping {sleep_s}s")
            time.sleep(sleep_s)


def download_layer_csv(year_code, out_path=None, chunk_size=300):
    url = BASE_URL.format(year_code)

    if out_path is None:
        out_path = f"nces_public_schools_{year_code}.csv"

    with requests.Session() as session:
        ids_payload = get_json(session, url, {
            "where": "1=1",
            "returnIdsOnly": "true",
            "f": "json",
        })
        object_ids = ids_payload.get("objectIds", [])
        object_ids.sort()

        print(f"Found {len(object_ids)} records for {year_code}. Downloading in chunks of {chunk_size}...")

        rows = []
        for i in range(0, len(object_ids), chunk_size):
            chunk = object_ids[i:i + chunk_size]

            payload = get_json(session, url, {
                "objectIds": ",".join(map(str, chunk)),
                "outFields": "*",
                "returnGeometry": "false",
                "f": "json",
            })

            feats = payload.get("features", [])
            rows.extend([f["attributes"] for f in feats])

            if (i // chunk_size) % 10 == 0:
                print(f"Fetched {min(i + chunk_size, len(object_ids))}/{len(object_ids)}")

            time.sleep(0.15)

        df = pd.DataFrame(rows)
        df.to_csv(out_path, index=False)
        print(f"Saved {len(df)} rows -> {out_path}")

def download_dp03():
    url = "https://api.census.gov/data/2022/acs/acs5/profile/groups/DP03.json"
    r = requests.get(url)
    r.raise_for_status()

    with open("DP03_2022.json", "w", encoding="utf-8") as f:
        f.write(r.text)

    print("Saved json file ")

if __name__ == "__main__":
    year_codes = ["1718", "1819", "1920", "2021", "2122", "2223"]

    for yc in year_codes:
        print(f"{yc}")
        download_layer_csv(yc)

    download_dp03()