from sqlalchemy import create_engine, text
from utils_SQL import db_connect

engine = db_connect()

with engine.connect() as conn:
    conn.execute(text(
        """

CREATE OR REPLACE VIEW combined_data AS
SELECT * FROM (
    -- 2017-2018
    SELECT
        "X"::text, "Y"::text, "OBJECTID"::text, "NCESSCH"::text, "SURVYEAR"::text,
        "STABR"::text, "LEAID"::text, "ST_LEAID"::text, "LEA_NAME"::text, "SCH_NAME"::text,
        "LSTREET1"::text, "LSTREET2"::text, "LSTREET3"::text, "LCITY"::text, "LSTATE"::text,
        "LZIP"::text, "LZIP4"::text, "PHONE"::text, "CHARTER_TEXT"::text, "MAGNET_TEXT"::text,
        "VIRTUAL"::text, "GSLO"::text, "GSHI"::text, "SCHOOL_LEVEL"::text,
        NULL::text AS "TITLEI", "STITLEI"::text, "STATUS"::text, "SCHOOL_TYPE_TEXT"::text,
        "SY_STATUS_TEXT"::text, "ULOCALE"::text, "NMCNTY"::text, "TOTFRL"::text,
        "FRELCH"::text, "REDLCH"::text, NULL::text AS "DIRECTCERT",
        "PK"::text, "KG"::text, "G01"::text, "G02"::text, "G03"::text, "G04"::text,
        "G05"::text, "G06"::text, "G07"::text, "G08"::text, "G09"::text, "G10"::text,
        "G11"::text, "G12"::text, "G13"::text, "UG"::text, "AE"::text,
        "TOTFENROL"::text, "TOTMENROL"::text, "TOTAL"::text, "MEMBER"::text, "FTE"::text,
        "STUTERATIO"::text,
        "AMALM"::text, "AMALF"::text, "AM"::text, "ASALM"::text, "ASALF"::text, "AS"::text,
        "BLALM"::text, "BLALF"::text, "BL"::text, "HPALM"::text, "HPALF"::text, "HP"::text,
        "HIALM"::text, "HIALF"::text, "HI"::text, "TRALM"::text, "TRALF"::text, "TR"::text,
        "WHALM"::text, "WHALF"::text, "WH"::text, "LATCOD"::text, "LONCOD"::text
    FROM public."PSD_2017_to_2018"

    UNION ALL

    -- 2018-2019
    SELECT
        "X"::text, "Y"::text, "OBJECTID"::text, "NCESSCH"::text, "SURVYEAR"::text,
        "STABR"::text, "LEAID"::text, "ST_LEAID"::text, "LEA_NAME"::text, "SCH_NAME"::text,
        "LSTREET1"::text, "LSTREET2"::text, NULL::text AS "LSTREET3", "LCITY"::text, "LSTATE"::text,
        "LZIP"::text, "LZIP4"::text, "PHONE"::text, "CHARTER_TEXT"::text, "MAGNET_TEXT"::text,
        "VIRTUAL"::text, "GSLO"::text, "GSHI"::text, "SCHOOL_LEVEL"::text,
        "TITLEI"::text, "STITLEI"::text, "STATUS"::text, "SCHOOL_TYPE_TEXT"::text,
        "SY_STATUS_TEXT"::text, "ULOCALE"::text, "NMCNTY"::text, "TOTFRL"::text,
        "FRELCH"::text, "REDLCH"::text, NULL::text AS "DIRECTCERT",
        "PK"::text, "KG"::text, "G01"::text, "G02"::text, "G03"::text, "G04"::text,
        "G05"::text, "G06"::text, "G07"::text, "G08"::text, "G09"::text, "G10"::text,
        "G11"::text, "G12"::text, "G13"::text, "UG"::text, "AE"::text,
        "TOTMENROL"::text, "TOTFENROL"::text, "TOTAL"::text, "MEMBER"::text, "FTE"::text,
        "STUTERATIO"::text,
        "AMALM"::text, "AMALF"::text, "AM"::text, "ASALM"::text, "ASALF"::text, "AS"::text,
        "BLALM"::text, "BLALF"::text, "BL"::text, "HPALM"::text, "HPALF"::text, "HP"::text,
        "HIALM"::text, "HIALF"::text, "HI"::text, "TRALM"::text, "TRALF"::text, "TR"::text,
        "WHALM"::text, "WHALF"::text, "WH"::text, "LATCOD"::text, "LONCOD"::text
    FROM public."PSD_2018_to_2019"

    UNION ALL

    -- 2020-2021
    SELECT
        "X"::text, "Y"::text, "OBJECTID"::text, "NCESSCH"::text, "SURVYEAR"::text,
        "STABR"::text, "LEAID"::text, "ST_LEAID"::text, "LEA_NAME"::text, "SCH_NAME"::text,
        "LSTREET1"::text, "LSTREET2"::text, NULL::text AS "LSTREET3", "LCITY"::text, "LSTATE"::text,
        "LZIP"::text, "LZIP4"::text, "PHONE"::text, "CHARTER_TEXT"::text, "MAGNET_TEXT"::text,
        "VIRTUAL"::text, "GSLO"::text, "GSHI"::text, "SCHOOL_LEVEL"::text,
        "TITLEI"::text, "STITLEI"::text, "STATUS"::text, "SCHOOL_TYPE_TEXT"::text,
        "SY_STATUS_TEXT"::text, "ULOCALE"::text, "NMCNTY"::text, "TOTFRL"::text,
        "FRELCH"::text, "REDLCH"::text, NULL::text AS "DIRECTCERT",
        "PK"::text, "KG"::text, "G01"::text, "G02"::text, "G03"::text, "G04"::text,
        "G05"::text, "G06"::text, "G07"::text, "G08"::text, "G09"::text, "G10"::text,
        "G11"::text, "G12"::text, "G13"::text, "UG"::text, "AE"::text,
        "TOTMENROL"::text, "TOTFENROL"::text, "TOTAL"::text, "MEMBER"::text, "FTE"::text,
        "STUTERATIO"::text,
        "AMALM"::text, "AMALF"::text, "AM"::text, "ASALM"::text, "ASALF"::text, "AS"::text,
        "BLALM"::text, "BLALF"::text, "BL"::text, "HPALM"::text, "HPALF"::text, "HP"::text,
        "HIALM"::text, "HIALF"::text, "HI"::text, "TRALM"::text, "TRALF"::text, "TR"::text,
        "WHALM"::text, "WHALF"::text, "WH"::text, "LATCOD"::text, "LONCOD"::text
    FROM public."PSD_2020_to_2021"

    UNION ALL

    -- 2021-2022
    SELECT
        "X"::text, "Y"::text, "OBJECTID"::text, "NCESSCH"::text, "SURVYEAR"::text,
        "STABR"::text, "LEAID"::text, "ST_LEAID"::text, "LEA_NAME"::text, "SCH_NAME"::text,
        "LSTREET1"::text, "LSTREET2"::text, NULL::text AS "LSTREET3", "LCITY"::text, "LSTATE"::text,
        "LZIP"::text, "LZIP4"::text, "PHONE"::text, "CHARTER_TEXT"::text, "MAGNET_TEXT"::text,
        "VIRTUAL"::text, "GSLO"::text, "GSHI"::text, "SCHOOL_LEVEL"::text,
        "TITLEI_TEXT"::text AS "TITLEI", "STITLEI"::text, "STATUS"::text, "SCHOOL_TYPE_TEXT"::text,
        "SY_STATUS_TEXT"::text, "ULOCALE"::text, "NMCNTY"::text, "TOTFRL"::text,
        "FRELCH"::text, "REDLCH"::text, "DIRECTCERT"::text,
        "PK"::text, "KG"::text, "G01"::text, "G02"::text, "G03"::text, "G04"::text,
        "G05"::text, "G06"::text, "G07"::text, "G08"::text, "G09"::text, "G10"::text,
        "G11"::text, "G12"::text, "G13"::text, "UG"::text, "AE"::text,
        "TOTMENROL"::text, "TOTFENROL"::text, "TOTAL"::text, "MEMBER"::text, "FTE"::text,
        "STUTERATIO"::text,
        "AMALM"::text, "AMALF"::text, "AM"::text, "ASALM"::text, "ASALF"::text, "AS"::text,
        "BLALM"::text, "BLALF"::text, "BL"::text, "HPALM"::text, "HPALF"::text, "HP"::text,
        "HIALM"::text, "HIALF"::text, "HI"::text, "TRALM"::text, "TRALF"::text, "TR"::text,
        "WHALM"::text, "WHALF"::text, "WH"::text, "LATCOD"::text, "LONCOD"::text
    FROM public."PSD_2021_to_2022"

    UNION ALL

    -- 2022-2023
    SELECT
        "X"::text, "Y"::text, "OBJECTID"::text, "NCESSCH"::text, "SURVYEAR"::text,
        "STABR"::text, "LEAID"::text, "ST_LEAID"::text, "LEA_NAME"::text, "SCH_NAME"::text,
        "LSTREET1"::text, "LSTREET2"::text, NULL::text AS "LSTREET3", "LCITY"::text, "LSTATE"::text,
        "LZIP"::text, "LZIP4"::text, "PHONE"::text, "CHARTER_TEXT"::text, NULL::text AS "MAGNET_TEXT",
        "VIRTUAL"::text, "GSLO"::text, "GSHI"::text, "SCHOOL_LEVEL"::text,
        NULL::text AS "TITLEI", NULL::text AS "STITLEI", "STATUS"::text, "SCHOOL_TYPE_TEXT"::text,
        "SY_STATUS_TEXT"::text, "ULOCALE"::text, "NMCNTY"::text, "TOTFRL"::text,
        "FRELCH"::text, "REDLCH"::text, "DIRECTCERT"::text,
        "PK"::text, "KG"::text, "G01"::text, "G02"::text, "G03"::text, "G04"::text,
        "G05"::text, "G06"::text, "G07"::text, "G08"::text, "G09"::text, "G10"::text,
        "G11"::text, "G12"::text, "G13"::text, "UG"::text, "AE"::text,
        "TOTMENROL"::text, "TOTFENROL"::text, "TOTAL"::text, "MEMBER"::text, "FTE"::text,
        "STUTERATIO"::text,
        "AMALM"::text, "AMALF"::text, "AM"::text, "ASALM"::text, "ASALF"::text, "AS"::text,
        "BLALM"::text, "BLALF"::text, "BL"::text, "HPALM"::text, "HPALF"::text, "HP"::text,
        "HIALM"::text, "HIALF"::text, "HI"::text, "TRALM"::text, "TRALF"::text, "TR"::text,
        "WHALM"::text, "WHALF"::text, "WH"::text, "LATCOD"::text, "LONCOD"::text
    FROM public."PSD_2022_to_2023"
) AS combined;

    """))
    conn.commit()