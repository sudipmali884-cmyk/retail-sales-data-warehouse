with stores as(
    select * from {{source('raw','stores')}}
),
cleaned_data as (
    select
        -- primary key
        trim(store_id) as store_id,
        -- store Information

        initcap(trim(store_name)) as store_name,
        initcap(trim(store_type)) as store_type,
        initcap(trim(manager_name)) as manager_name,

        -- phone

        case
            when regexp_like(trim(phone), '^[6-9][0-9]{10}$')
                then trim(phone)
            when regexp_like(trim(phone), '^[6-9][0-9]{9}$')
                then trim(phone)
            else '8999018894'
        end as phone,

--        / email
        case
            when email is null then 'notemail'
            when trim(email) = '' then null

            when regexp_like(lower(trim(email)),
            '^[a-z0-9._%-]+@[a-z0-9.-]+\.[a-z]{2,}$')

               then lower(trim(email))
           else null
        end as email,

--        address

        case
            when trim(address)='' then null
            else initcap(trim(address))
        end as address,

        -- location
        initcap(trim(city)) as city,
        initcap(trim(state)) as state,

        -- postal code

        case
            when regexp_like(trim(postal_code),'^[0-9]{6}$')
                then trim(postal_code)

            else null
        end as postal_code,

--        dates

        try_to_date(opening_date) as opening_date,
        try_to_date(created_at) as created_at,
        try_to_date(updated_at) as updated_at,

        -- status

        case
            when upper(trim(status))='ACTIVE'
                then 'Active'
            when upper(trim(status))='CLOSED'
                then 'Closed'
            when upper(trim(status))='RENOVATION'
                then 'Renovation'
        end as status

    from stores
),

deduplicated as(
    select * from cleaned_data
    qualify row_number() over(
    partition by store_id
    order by updated_at desc )=1
)
select * from deduplicated

