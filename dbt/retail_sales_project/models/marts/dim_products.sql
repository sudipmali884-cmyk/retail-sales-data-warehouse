with products as(
    select * from {{ ref('stg_products')}}
)

select
--    product_id,
--    product_name,
--    category,
--    sub_category,
--    brand,
--    supplier,
--    cost_price,
--    margin,
--    unit_price,
--    (unit_price - cost_price) as profit_margin,
--    barcode,
--    weight,
--    launch_date,
--    status,
--    created_at,
--    updated_at
    *

from products

--Reports that use this dimension
--
--Power BI can create reports like:
--
--✅ Sales by Category
--✅ Sales by Brand
--✅ Top Selling Products
--✅ Profit by Product
--✅ Profit by Category
--✅ Product Launch Analysis
--✅ Active vs Inactive Products


-- sales by brand
--select p.brand ,sum(s.total_amount) as total_amount from products p join sales s on s.product_id = p.product_id group by brand;
--select p.brand , sum(s.quantity) as total_quantity from products p join sales s on s.product_id = p.product_id group by brand;
--select * from products;
--
--
---- top products by sales
--select p.product_name , max(s.quantity) as top_products_selled from stg_products p join stg_sales s on s.product_id=p.product_id group by product_name;
--select p.product_name , sum(s.quantity) as most_selled_products from stg_products p join stg_sales s on s.product_id=p.product_id group by product_name order by most_selled_products desc;
--select sum(quantity) from sales group by all;
