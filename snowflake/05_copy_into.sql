-- =====================================================
-- copy into
-- =====================================================


-- CUSTOMERS

copy into customers from @retail_stage/customers.csv file_format=(format_name='csv_format');

-- 2. PRODUCTS

copy into products from @retail_stage/products.csv file_format=(format_name='csv_format');

-- 3. EMPLOYEES 

copy into employees from @retail_stage/employees.csv file_format=(format_name='csv_format');

-- 4. STORES

copy into stores from @retail_stage/stores.csv file_format=(format_name='csv_format');

-- 5. INVENTORY

copy into inventory from @retail_stage/inventory.csv file_format=(format_name='csv_format');

-- 6. PROMOTIONS 

copy into promotions from @retail_stage/promotions.csv file_format=(format_name='csv_format');

-- 7. RETURNS 

COPY into returns from @retail_stage/returns.csv file_format=(format_name='csv_format');

-- 8. SALES 

copy into sales from @retail_stage/sales.csv file_format=(format_name='csv_format');

-- =====================================================
-- VERIFY
-- =====================================================

LIST @RETAIL_STAGE;