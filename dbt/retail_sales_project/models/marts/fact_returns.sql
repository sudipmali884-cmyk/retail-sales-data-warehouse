with returns as(
    select * from {{ ref('int_returns')}}
)
select
    -- primary key
    return_id,
    -- related sale
    sale_id,

    -- dimension keys
    customer_id,
    store_id,
    employee_id,
    product_id,

    -- date
    return_date,

    -- measures
    return_quantity,
    refund_amount,

    -- business attributes
    return_reason,
    refund_method,
    return_status,

    -- audit columns

    created_at,
    updated_at
from returns


--Why doesn't fact_returns contain customer name?
--It stores only:
--
--Keys
--Measures
--Business Attributes
--
--Descriptive information comes from dimension tables.
