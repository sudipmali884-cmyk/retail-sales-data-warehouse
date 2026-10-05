with inventory as(
    select * from {{source('raw','inventory')}}
),

cleaned_data as (
    select
    trim(inventory_id) as inventory_id,

    case
        when regexp_like (trim(store_id),'^STR[0-9]{6}$')
            then trim(store_id)
        else 'Wrong Store Id'
    end as store_id,

    case
        when regexp_like(trim(product_id), '^PRO[0-9]{6}$')
            then trim(product_id)
        else 'Wrong Product ID'
    end as product_id,

    --=========================
    -- Quantity
    --=========================
    case
        when quantity >= 0
            then quantity
        else null
    end as quantity,

    --=========================
    -- Reorder Level
    --=========================
    case
        when reorder_level >= 0
            then reorder_level
        else null
    end as reorder_level,

    --=========================
    -- Inventory Value
    --=========================
    case
        when inventory_value >= 0
            then inventory_value
        else null
    end as inventory_value,

    -- status
    case
        when upper(trim(status))='AVAILABLE'
            then 'Available'
        when upper(trim(status))='LOW STOCK'
            then 'Low Stock'

        when upper(trim(status))='OUT OF STOCK'
            then 'Out Of Stock'

        else 'Unknown'
    end as status,
    --=========================
    -- Dates
    --=========================
    case
        when try_to_date(last_stock_date) > current_date
            then null
        else try_to_date(last_stock_date)
    end as last_stock_date,

    try_to_date(created_at) as created_at,

    try_to_date(updated_at) as updated_at

from inventory

),

deduplicated as (

    select *

    from cleaned_data

    qualify row_number() over (

        partition by inventory_id
--            store_id,
--            product_id

        order by updated_at desc

    ) = 1

)

select * from deduplicated
