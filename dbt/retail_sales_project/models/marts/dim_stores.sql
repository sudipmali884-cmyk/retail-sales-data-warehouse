--This dimension contains all the descriptive information about stores. The fact_sales table will only store the store_id,
--while Power BI will use this dimension to display store details.

with stores as(
    select * from {{ ref('stg_stores')}}
)

select
--
--    --------------------------------------------------
--    -- Primary Key
--    --------------------------------------------------
--
--    store_id,
--
--    --------------------------------------------------
--    -- Store Information
--    --------------------------------------------------
--
--    store_name,
--
--    store_type,
--
--    manager_name,
--
--    --------------------------------------------------
--    -- Contact Information
--    --------------------------------------------------
--
--    phone_number,
--
--    email,
--
--    --------------------------------------------------
--    -- Location
--    --------------------------------------------------
--
--    city,
--
--    state,
--
--    postal_code,
--
--    --------------------------------------------------
--    -- Business Information
--    --------------------------------------------------
--
--    opening_date,
--
--    store_status,
--
--    --------------------------------------------------
--    -- Audit Columns
--    --------------------------------------------------
--
--    created_at,
--
--    updated_at

* from stores


--Power BI can build reports such as:
--
--✅ Sales by Store
--✅ Sales by City
--✅ Sales by State
--✅ Sales by Store Type
--✅ Top 10 Stores by Revenue
--✅ Top 10 Stores by Profit
--✅ Active vs Inactive Stores
--✅ Monthly Store Performance