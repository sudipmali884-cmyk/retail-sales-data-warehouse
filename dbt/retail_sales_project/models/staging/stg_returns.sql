with returns as (
    select * from {{ source('raw','returns')}}
),

cleaned_data as(
    select
        trim(return_id) as return_id,

        -- foreign key
        case
            when regexp_like(trim(sale_id),'^SALE[0-9]{8}$')
                then trim(sale_id)
            else null
        end as sale_id,
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
            when regexp_like(trim(employee_id), '^EMP[0-9]{6}$')
                then trim(employee_id)
            else null
        end as employee_id,

        case
            when regexp_like(trim(product_id),'^PRO[0-9]{6}$')
                then trim(product_id)
            else null
        end as product_id,

        -- return date
        case
            when try_to_date(return_date) > current_date
                then null
            else try_to_date(return_date)
        end as return_date,

        case
            when trim(return_reason)='' then null
            else initcap(trim(return_reason))
        end as return_reason,

        case
            when return_quantity > 0
                then return_quantity
            else null
        end as return_quantity,

        case
            when refund_amount >= 0
                then refund_amount
            else null
        end as refund_amount,

        case
            when upper(trim(refund_method))='CASH'
                then 'Cash'
            when upper(trim(refund_method))='UPI'
                then 'UPI'
            when upper(trim(refund_method))='DEBIT CARD'
                then 'Debit Card'
            when upper(trim(refund_method))='NET BANKING'
                then 'Net Banking'
            else 'Unknown'
        end as refund_method,

        case
            when upper(trim(return_status))='APPROVED'
                then 'Approved'
            when upper(trim(return_status))='PENDING'
                then 'Pending'
            when upper(trim(return_status))='REJECTED'
                then 'Rejected'
            else 'Unknown'
        end as return_status,

        try_to_date(created_at) as created_at,
        try_to_date(updated_at) as updated_at
    from returns
),
deduplicated as (
    select * from cleaned_data
    qualify row_number() over(
        partition by return_id
        order by updated_at desc
    )=1
)

select * from deduplicated