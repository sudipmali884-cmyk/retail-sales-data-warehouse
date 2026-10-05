--What is this model doing?
--
--This model creates a clean fact_sales table.
--
--It ensures that every sale has:
--
--✅ Valid customer
--✅ Valid store
--✅ Valid employee
--✅ Valid product
--✅ Positive quantity
--✅ Positive price
--✅ Valid sale date
--
--If any of these are invalid, that sale is removed.
--
--Q. Why not create fact_sales directly from stg_sales?
--
--Answer:
--
--Because stg_sales only standardizes and cleans data formats.
--
--The Intermediate Layer applies business rules, validates relationships, and filters invalid transactions.
--
--Keeping these responsibilities separate makes the project easier to maintain and aligns with dbt best practices.
--

with sales as(
    select * from {{ ref('stg_sales')}}
),
customers as(
    select customer_id from {{ ref('stg_customers')}}
),

stores as (
    select  store_id from {{ ref('stg_stores')}}
),

employees as (
    select employee_id from {{ ref('stg_employees')}}
),

products as (
    select product_id from {{ ref('stg_products')}}
),

final as (
select
    s.* from sales s

    inner join customers c
    on s.customer_id = c.customer_id

    inner join stores st
    on s.store_id = st.store_id

    inner join employees e
    on s.employee_id = e.employee_id

    inner join products p
    on s.product_id = p.product_id

    where

        quantity > 0
        and unit_price > 0

        and gross_amount >= 0

        and total_amount >= 0

        and sale_date is not null
)

select * from final