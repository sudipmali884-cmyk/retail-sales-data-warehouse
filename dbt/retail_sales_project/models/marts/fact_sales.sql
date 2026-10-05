with sales as(
    select * from {{ ref('int_sales')}}
)

select
    -- primary key
    sale_id,

    -- date
    sale_date,

    -- dimension keys

    customer_id,
    store_id,
    employee_id,
    product_id,

    -- measures

    quantity,
    unit_price,
    gross_amount,
    discount_percentage,
    discount_amount,
    tax_amount,
    total_amount,
    profit,

    -- business attributes

    payment_method,
    sales_status,

    -- aduit columns

    created_at,
    updated_at
from sales