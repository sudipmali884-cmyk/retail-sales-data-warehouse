-- =====================================================
-- Warehouse
-- =====================================================
create warehouse retail_wh
with warehouse_size='xsmall'
auto_suspend=60
auto_resume=TRUE;

use warehouse retail_wh;
-- =====================================================
-- Database
-- =====================================================

create database retail_db;
use database retail_db;


create schema raw;
create schema staging;
create schema mart;

use schema raw;
