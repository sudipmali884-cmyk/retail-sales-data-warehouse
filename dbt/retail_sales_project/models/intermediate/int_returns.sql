--It will ensure:
--
--Sale exists
--Customer exists
--Product exists
--Store exists
--Employee exists
--Return quantity > 0
--Refund amount ≥ 0
--Return date is valid
--
--After that, we'll start building the dimension tables, beginning with dim_customers.sql

with returns as (
    select * from {{ ref('stg_returns')}}
),

sales as (
    select sale_id  from {{ ref('stg_sales')}}
),
customers as (
    select customer_id from  {{ ref('stg_customers')}}
),

stores as (
    select store_id from {{ ref('stg_stores')}}
),

employees as (
    select employee_id from  {{ ref('stg_employees')}}
),

products as (
    select product_id  from {{ ref('stg_products')}}
),

final as (
    select r.*
    from returns r
    inner join sales s
    on r.sale_id = s.sale_id
    inner join customers c
    on r.customer_id= c.customer_id
    inner join stores st
    on r.store_id = st.store_id
    inner join employees e
    on r.employee_id = e.employee_id
    inner join products p
    on r.product_id = p.product_id
    where
        return_quantity > 0
        and refund_amount >= 0
        and return_date is not null

)

select * from final