USE DATABASE retail_sales_db;
USE SCHEMA raw;

-- =====================================================
-- 1. CUSTOMERS
-- =====================================================

CREATE OR REPLACE TABLE customers (

    customer_id STRING,

    first_name STRING,

    last_name STRING,

    gender STRING,

    date_of_birth DATE,

    phone_number STRING,

    email STRING,

    city STRING,

    state STRING,

    postal_code STRING,

    registration_date DATE,

    customer_status STRING,

    created_at DATE,

    updated_at DATE

);

-- =====================================================
-- 2. STORES
-- =====================================================

CREATE OR REPLACE TABLE stores (

    store_id STRING,

    store_name STRING,

    store_type STRING,

    manager_name STRING,

    phone_number STRING,

    email STRING,

    city STRING,

    state STRING,

    postal_code STRING,

    opening_date DATE,

    store_status STRING,

    created_at DATE,

    updated_at DATE

);

-- =====================================================
-- 3. EMPLOYEES
-- =====================================================

CREATE OR REPLACE TABLE employees (

    employee_id STRING,

    employee_name STRING,

    gender STRING,

    phone STRING,

    email STRING,

    department STRING,

    designation STRING,

    salary STRING,

    hire_date DATE,

    status STRING,

    store_id STRING,

    created_at DATE,

    updated_at DATE

);

-- =====================================================
-- 4. PRODUCTS
-- =====================================================

CREATE OR REPLACE TABLE products (

    product_id STRING,

    product_name STRING,

    category STRING,

    sub_category STRING,

    brand STRING,

    supplier STRING,

    cost_price STRING,

    unit_price STRING,

    barcode STRING,

    weight STRING,

    launch_date DATE,

    status STRING,

    created_at DATE,

    updated_at DATE

);

-- =====================================================
-- 5. INVENTORY
-- =====================================================

CREATE OR REPLACE TABLE inventory (

    inventory_id STRING,

    store_id STRING,

    product_id STRING,

    quantity STRING,

    reorder_level STRING,

    inventory_value STRING,

    status STRING,

    last_stock_date DATE,

    created_at DATE,

    updated_at DATE

);

-- =====================================================
-- 6. PROMOTIONS
-- =====================================================

CREATE OR REPLACE TABLE promotions (

    promotion_id STRING,

    product_id STRING,

    promotion_name STRING,

    promotion_type STRING,

    category STRING,

    brand STRING,

    discount_percentage STRING,

    start_date DATE,

    end_date DATE,

    status STRING,

    created_at DATE,

    updated_at DATE

);

-- =====================================================
-- 7. SALES
-- =====================================================

CREATE OR REPLACE TABLE sales (

    sale_id STRING,

    sale_date DATE,

    customer_id STRING,

    store_id STRING,

    employee_id STRING,

    product_id STRING,

    quantity STRING,

    unit_price STRING,

    gross_amount STRING,

    discount_percentage STRING,

    discount_amount STRING,

    tax_amount STRING,

    total_amount STRING,

    profit STRING,

    payment_method STRING,

    sales_status STRING,

    created_at DATE,

    updated_at DATE

);

-- =====================================================
-- 8. RETURNS
-- =====================================================

CREATE OR REPLACE TABLE returns (

    return_id STRING,

    sale_id STRING,

    customer_id STRING,

    store_id STRING,

    employee_id STRING,

    product_id STRING,

    return_date DATE,

    return_reason STRING,

    return_quantity STRING,

    refund_amount STRING,

    refund_method STRING,

    return_status STRING,

    created_at DATE,

    updated_at DATE

);