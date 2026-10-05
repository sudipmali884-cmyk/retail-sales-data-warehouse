USE DATABASE retail_sales_db;

USE SCHEMA raw;

-- =====================================================
-- CSV FILE FORMAT
-- =====================================================

CREATE OR REPLACE FILE FORMAT csv_format

TYPE = CSV

SKIP_HEADER = 1

FIELD_OPTIONALLY_ENCLOSED_BY = '"'

NULL_IF = ('NULL','','null')

EMPTY_FIELD_AS_NULL = TRUE

TRIM_SPACE = TRUE;

-- =====================================================
-- VERIFY
-- =====================================================

SHOW FILE FORMATS;