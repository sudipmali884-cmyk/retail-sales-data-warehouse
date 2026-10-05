with employees as (
    select * from {{ ref('stg_employees')}}
)

select
* from employees

--Power BI can build reports such as:
--
--✅ Sales by Employee
--✅ Top Performing Employees
--✅ Employee Revenue Ranking
--✅ Sales by Department
--✅ Employee Count by Store
--✅ Employee Count by Department
--✅ Average Sales per Employee
--✅ Active vs Inactive Employees