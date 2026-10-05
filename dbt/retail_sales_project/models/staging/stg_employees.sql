with employees as(
    select  * from {{ source('raw','employees')}}
),

cleaned_date as (
    select
        -- primary key
        trim(employee_id) as employee_id,
        -- employee details
        initcap(trim(employee_name)) as employee_name,

        case
            when upper(trim(gender))='MALE' then 'Male'
            when upper(trim(gender))='FEMALE' then 'Female'
            else 'Transgender'
        end as gender,

        initcap(trim(designation)) as designation,
        case
            when trim(department) ='' then null
            else initcap(trim(department))
            end as department,
        -- store
        case
            when regexp_like(trim(store_id), '^STR[0-9]{6}$')
                then trim(store_id)
            else null

        end as store_id,

        initcap(trim(city)) as city,
        initcap(trim(state)) as state,

        -- contact
        case
            when regexp_like(trim(phone), '^[6-9][0-9]{9}$')
                then trim (phone)
            else null
        end as phone,

        case
            when email is null then 'No Email'
            when trim(email)='' then 'No Email'
            when regexp_like(lower(trim(email)),
            '^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
            )
            then lower(trim(email))
            else 'No Email'
        end as email,

        -- salary
        case
            when salary > 0 then salary
            else 'No Salary'

        end as salary,

        -- hire date
        case
            when try_to_date(hire_date)> current_date
                then null
            else try_to_date(hire_date)
        end as hire_date,

        --status
        case
            when upper(trim(status))='ACTIVE'
                then 'Active'
            when upper(trim(status))='RESIGNED'
                then 'Resigned'
            when upper (trim(status))='ON LEAVE'
                then 'On Leave'
            else 'Unknown'
        end as status,

        try_to_date(created_at) as created_at,
        try_to_date(updated_at) as updated_at
    from employees
),

deduplicated as (
    select * from cleaned_date
    qualify row_number()
    over(
    partition by employee_id
    order by updated_at desc
    )=1
)

select * from deduplicated