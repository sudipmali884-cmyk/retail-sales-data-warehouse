with products as (

    select *
    from {{ source('raw','products') }}

),

cleaned as (

    select

        --=========================
        -- Primary Key
        --=========================
        trim(product_id) as product_id,

        --=========================
        -- Product
        --=========================
        case
            when product_name is null then 'Name is Null'
            when trim(product_name)='' then 'Name is Null'
            else initcap(trim(product_name))
        end as product_name,

        --=========================
        -- Category
        --=========================
        case
            when upper(trim(category))='GROCERY' then 'Grocery'
            when upper(trim(category))='DAIRY' then 'Dairy'
            when upper(trim(category))='BEVERAGES' then 'Beverages'
            when upper(trim(category))='SNACKS' then 'Snacks'
            when upper(trim(category))='PERSONAL CARE' then 'Personal Care'
            when upper(trim(category))='HOUSEHOLD' then 'Household'
            else null
        end as category,

        --=========================
        -- Sub Category
        --=========================
        case
            when trim(sub_category)='' then 'No Category'
            else initcap(trim(sub_category))
        end as sub_category,

        --=========================
        -- Brand
        --=========================
        case
            when trim(brand)='' then null
            else initcap(trim(brand))
        end as brand,

        --=========================
        -- Supplier
        --=========================
        case
            when trim(supplier)='' then null
            else initcap(trim(supplier))
        end as supplier,

        --=========================
        -- Prices
        --=========================
        case
            when cost_price > 0
                then cost_price
            else null
        end as cost_price,

        case
            when margin >= 0
                then margin
            else null
        end as margin,

        case
            when unit_price > 0
                then unit_price
            else null
        end as unit_price,

        --=========================
        -- Barcode
        --=========================
        case
            when regexp_like(trim(barcode),'^[0-9]{12}$')
                then trim(barcode)
            else null
        end as barcode,

        --=========================
        -- Weight
        --=========================
        case
            when weight > 0
                then weight
            else null
        end as weight,

        --=========================
        -- Launch Date
        --=========================
        case
            when try_to_date(launch_date) > current_date
                then null
            else try_to_date(launch_date)
        end as launch_date,

        --=========================
        -- Status
        --=========================
        case
            when upper(trim(status))='ACTIVE'
                then 'Active'

            when upper(trim(status))='DISCONTINUED'
                then 'Discontinued'

            else 'Unknown'
        end as status,

        try_to_date(created_at) as created_at,

        try_to_date(updated_at) as updated_at

    from products

),

deduplicated as (

    select *

    from cleaned

    qualify row_number() over(

        partition by product_id

        order by updated_at desc

    ) = 1

)

select *
from deduplicated