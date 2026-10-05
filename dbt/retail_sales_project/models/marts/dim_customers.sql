with customers as (
    select * from {{ ref('stg_customers')}}
)
select

    -- primary key
    customer_id,
    -- customer Information
    first_name,
    last_name,
    concat( first_name , ' ', last_name) as customer_name,
    gender,
    date_of_birth,

    phone_number,
    email,
    city,
    state,
    postal_code,

    registration_date,
    customer_status,

    created_at,
    updated_at

from customers
