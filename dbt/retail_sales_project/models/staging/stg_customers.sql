with customers as(
    select * from {{source('raw','customers')}}
),
cleaned as(
select
-- primary key

    trim(customer_id) as customer_id,
    initcap(trim(first_name)) as first_name,
    initcap(trim(last_name)) as last_name,

    -- gender
    case
    when upper(trim(gender))='MALE'
    then 'Male'
    when upper(trim(gender))='FEMALE'
    then 'Female'
    else null
    end as gender,
--    dob
    try_to_date(date_of_birth) as date_of_birth,

--    phone
    case
        when regexp_like(trim(phone_number),'^[6-9][0-9]{9}$')
            then trim(phone_number)
        else '9423348999'
    end as phone_number,
--    email
    case
        when email is null then 'unknown@gmail.com'
        when trim(email) = '' then 'unknown@gmail.com'
        else lower(trim(email))
    end as email,
--    city
    case
        when trim(city)='' then null
        else initcap(trim(city))
    end as city,

--    state

    initcap(trim(state)) as state,

-- postal code
    case
        when regexp_like(trim(postal_code), '^[0-9]{6}$')
            then trim(postal_code)
        else null
    end as postal_code,
--    Registration Date
    try_to_date(registration_date)  AS registration_date,

--    status
    case
        when upper(trim(customer_status))='ACTIVE'
        then 'Active'

        when upper(trim(customer_status))='INACTIVE'
        THEN 'Inactive'
    else null
    end as customer_status,

    -- dates
    try_to_date(created_at) as created_at,
    try_to_date(updated_at) as updated_at
    from customers
    ),
deduplicated as (
    select * from cleaned
    qualify row_number() over(
    partition by customer_id
    order by updated_at desc)=1
)
--deduplicated as (
--    select * from cleaned
--    qualify row_number() over(
--    partition by
--        customer_id,
--        first_name,
--        last_name,
--        gender,
--        date_of_birth,
--        phone_number,
--        email,
--        city,
--        state,
--        postal_code,
--        registration_date,
--        customer_status,
--        created_at,
--        updated_at
--    order by customer_id desc
--    )=1
--
--) -- this will remove all duplicate racords but in lur we also do some duplicate customers id  that's why we use our first deduplicated
select * from deduplicated