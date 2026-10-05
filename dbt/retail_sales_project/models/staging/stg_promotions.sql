with promotions as(
    select * from {{source('raw','promotions')}}
),
cleaned_data as(
    select
        nullif(trim(promotion_id), '') as promotion_id,

        case
            when regexp_like (trim(product_id), '^PRO[0-9]{6}$')
                then trim(product_id)
            else null
        end as product_id,
        case
            when promotion_name is null then null
            when trim(promotion_name)='' then null
            else initcap(trim(promotion_name))
        end as promotion_name,
        --=========================
        -- Promotion Type
        --=========================
        case
            when upper(trim(promotion_type))='FLAT DISCOUNT'
                then 'Flat Discount'

            when upper(trim(promotion_type))='PERCENTAGE DISCOUNT'
                then 'Percentage Discount'

            when upper(trim(promotion_type))='BUY ONE GET ONE'
                then 'Buy One Get One'

            when upper(trim(promotion_type))='FESTIVAL OFFER'
                then 'Festival Offer'

            when upper(trim(promotion_type))='CLEARANCE SALE'
                then 'Clearance Sale'

            else 'Unknown'
        end as promotion_type,

        -- category
        case
            when trim(category)='' then null
            else initcap(trim(category))
        end as category,

        -- brand
        case
            when trim(brand)='' then null
            else initcap(trim(brand))
        end as brand,


        -- discount Percentage
        case
            when discount_percentage between 0 and 100
                then discount_percentage
            else 'No Discount'
        end as discount_percentage,

        -- dates
        case
            when upper(trim(status))='ACTIVE'
                then 'Active'
            when upper(trim(status))='EXPIRED'
                then 'Expired'

            when upper(trim(status))='SCHEDULED'
                then 'Scheduled'

            else 'Unknown'
        end as status,

        case
            when try_to_date(end_date) >= try_to_date(start_date)
                then try_to_date(end_date)
            else null
        end as end_date,

        try_to_date(created_at) as created_at,
        try_to_date(updated_at) as updated_at

    from promotions

),

deduplicated as(
    select * from cleaned_data
    qualify row_number() over(
        partition by promotion_id
        order by updated_at desc
    )=1
)
select * from deduplicated
