with sales as (

    select *
    from {{ source('raw','sales') }}

),

cleaned as (

    select

        --=========================
        -- Primary Key
        --=========================
        trim(sale_id) as sale_id,

        --=========================
        -- Foreign Keys
        --=========================
        case
            when regexp_like(trim(customer_id),'^CUST[0-9]{6}$')
                then trim(customer_id)
            else null
        end as customer_id,

        case
            when regexp_like(trim(store_id),'^STR[0-9]{6}$')
                then trim(store_id)
            else null
        end as store_id,

        case
            when regexp_like(trim(employee_id),'^EMP[0-9]{6}$')
                then trim(employee_id)
            else null
        end as employee_id,

        case
            when regexp_like(trim(product_id),'^PRO[0-9]{6}$')
                then trim(product_id)
            else null
        end as product_id,

        --=========================
        -- Quantity
        --=========================
        case
            when quantity > 0
                then quantity
            else null
        end as quantity,

        --=========================
        -- Prices
        --=========================
        case
            when unit_price > 0
                then unit_price
            else null
        end as unit_price,

        case
            when cost_price > 0
                then cost_price
            else null
        end as cost_price,

        case
            when gross_amount >= 0
                then gross_amount
            else null
        end as gross_amount,

        case
            when discount_percentage between 0 and 100
                then discount_percentage
            else null
        end as discount_percentage,

        case
            when discount_amount >= 0
                then discount_amount
            else null
        end as discount_amount,

        case
            when tax_amount >= 0
                then tax_amount
            else null
        end as tax_amount,

        case
            when total_amount >= 0
                then total_amount
            else null
        end as total_amount,

        profit,

        --=========================
        -- Payment Method
        --=========================
        case
            when upper(trim(payment_method))='CASH'
                then 'Cash'

            when upper(trim(payment_method))='UPI'
                then 'UPI'

            when upper(trim(payment_method))='CREDIT CARD'
                then 'Credit Card'

            when upper(trim(payment_method))='DEBIT CARD'
                then 'Debit Card'

            when upper(trim(payment_method))='NET BANKING'
                then 'Net Banking'

            else 'Unknown'
        end as payment_method,

        --=========================
        -- Sales Status
        --=========================
        case
            when upper(trim(sales_status))='COMPLETED'
                then 'Completed'

            when upper(trim(sales_status))='RETURNED'
                then 'Returned'

            when upper(trim(sales_status))='CANCELLED'
                then 'Cancelled'

            else 'Unknown'
        end as sales_status,

        --=========================
        -- Dates
        --=========================
        case
            when try_to_date(sale_date) > current_date
                then null
            else try_to_date(sale_date)
        end as sale_date,

        try_to_date(created_at) as created_at,

        try_to_date(updated_at) as updated_at

    from sales

),

validated as (

    select

        *,

        case
            when unit_price >= cost_price
                then true
            else false
        end as valid_price

    from cleaned

),

deduplicated as (

    select *

    from validated

    qualify row_number() over(

        partition by sale_id

        order by updated_at desc

    ) = 1

)

select *
from deduplicated