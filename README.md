# Retail Sales Data Warehouse & Analytics

An end-to-end **Retail Sales Data Warehouse and Business Intelligence project** built using **Python, Snowflake, dbt, SQL, and Power BI**.

The project demonstrates the complete data pipeline from **data generation and data quality handling → Snowflake → dbt transformations → dimensional modeling → Power BI dashboards**.

---

## 🚀 Project Architecture

```text
Python
   ↓
CSV Files
   ↓
Snowflake RAW
   ↓
dbt STAGING
   ↓
dbt INTERMEDIATE
   ↓
dbt MARTS
   ↓
Power BI
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Faker
* SQL
* Snowflake
* dbt
* Power BI
* Git & GitHub

---

## 📊 Dataset

The project contains realistic retail datasets for:

* Customers
* Stores
* Employees
* Products
* Inventory
* Promotions
* Sales
* Returns

The datasets are generated using Python and Faker while maintaining relationships between entities through IDs and foreign keys.

---

## 🧹 Data Quality

The project also simulates common real-world data quality problems, including:

* Duplicate records
* Missing values
* Invalid values
* Invalid phone numbers
* Incorrect formats
* Inconsistent text casing
* Invalid categorical values

These issues are handled during the data transformation process.

---

## ❄️ Snowflake

The raw CSV files are loaded into Snowflake.

Main activities include:

* Database and schema creation
* Tables
* Internal stages
* `COPY INTO`


---

## 🔄 dbt Transformation

dbt is used to transform raw retail data into an analytics-ready data warehouse.

### dbt Layers

```text
RAW
 ↓
STAGING
 ↓
INTERMEDIATE
 ↓
MARTS
```

### Staging

Cleans and standardizes raw data.

Examples:

* Removing duplicates
* Handling NULL values
* Standardizing columns
* Correcting data types
* Cleaning invalid data

### Intermediate

Creates reusable business transformations and combines related datasets.

### Marts

Creates analytics-ready fact and dimension tables.

---

## ⭐ Data Warehouse Model

The project follows a **Star Schema**.

### Dimension Tables

```text
dim_customers
dim_products
dim_stores
dim_employees
dim_promotions
```

### Fact Tables

```text
fact_sales
fact_returns
```

Simplified model:

```text
                  dim_customers
                        |
                        |
dim_products ---- fact_sales ---- dim_stores
                        |
                        |
                 dim_employees
                        |
                        |
                 dim_promotions


                  fact_returns
                 /     |      \
                /      |       \
     dim_customers dim_products dim_stores
```

---

# 📈 Power BI Dashboards

The project contains seven analytical dashboards.

### 1. Executive Dashboard

Provides a high-level business overview.

Includes:

* Total Revenue
* Total Profit
* Total Orders
* Quantity Sold
* Total Customers
* Profit Margin
* Return Rate
* Revenue Trend
* Sales by Category
* Sales by State
* Top Products
* Top Stores

---

### 2. Sales Dashboard

Analyzes overall sales performance.

Includes:

* Monthly Sales Trend
* Revenue vs Profit
* Sales by Brand
* Sales by Category
* Top Products
* Top Employees
* Top Stores
* Payment Method Analysis

---

### 3. Customer Analytics

Analyzes customer behavior.

Includes:

* Total Customers
* Active Customers
* Inactive Customers
* Customer Registration Trend
* Customers by Gender
* Customers by State
* Customers by City
* Top Customers by Revenue
* Customer Status Distribution

---

### 4. Product Analytics

Analyzes product performance.

Includes:

* Total Products
* Active Products
* Revenue by Category
* Revenue by Brand
* Top Products by Revenue
* Top Products by Profit
* Category Contribution
* Brand Contribution
* Product Performance

---

### 5. Store Performance

Analyzes store-level performance.

Includes:

* Total Stores
* Active Stores
* Revenue by State
* Revenue by City
* Top Stores
* Bottom Stores
* Revenue vs Profit
* Store Performance Table

---

### 6. Employee Performance

Analyzes employee sales performance.

Includes:

* Total Employees
* Active Employees
* Revenue by Department
* Revenue by Designation
* Top Employees
* Bottom Employees
* Revenue vs Profit
* Employee Performance Table

---

### 7. Returns & Promotions

Analyzes returns and promotional performance.

Includes:

* Total Returns
* Return Rate
* Total Refund
* Average Discount
* Promotion Revenue
* Return Trend
* Returns by Category
* Return Reasons
* Promotion Revenue vs Profit
* Discount vs Revenue

---

# 🔄 End-to-End Workflow

### Step 1 — Generate Data

Python scripts generate the retail datasets.

Python → CSV


### Step 2 — Load Raw Data

CSV files are loaded into Snowflake RAW tables.

```text
CSV → Snowflake RAW
```

### Step 3 — Transform Data

dbt transforms and cleans the raw data.

```text
RAW
 ↓
STAGING
 ↓
INTERMEDIATE
 ↓
MARTS
```

### Step 4 — Build Data Warehouse

Fact and dimension tables are created using a Star Schema.

### Step 5 — Connect Power BI

Power BI connects to the analytics-ready Snowflake/dbt models.

### Step 6 — Build Dashboards

Business KPIs and interactive dashboards are created for different business teams.

---

# 💼 Business Problems Solved

The project helps answer questions such as:

* What is the total revenue and profit?
* Which products generate the most revenue?
* Which stores perform best?
* Which states generate the highest sales?
* Which customers generate the most revenue?
* Which employees perform best?
* Which categories are most profitable?
* What are the most common return reasons?
* How effective are promotions?
* How do discounts affect revenue?
* What is the overall return rate?

---

# 🎯 Key Learning Outcomes

Through this project, I practiced:

* Python data generation
* Pandas data processing
* Data quality handling
* SQL
* Snowflake data warehousing
* Data loading
* dbt transformations
* Star Schema modeling
* Fact and Dimension tables
* Data testing
* Data security concepts
* DAX
* Power BI data modeling
* Power BI dashboard development
* Git and GitHub

---


# 👨‍💻 Project Type

**End-to-End Data Engineering & Business Intelligence Project**

### Suitable for demonstrating skills for:

* Data Engineer
* Junior Data Engineer
* Analytics Engineer
* BI Developer
* Data Analyst

---

## ⭐ Author

**Sudip Mali**

GitHub: https://github.com/sudipmali884-cmyk
