# E-Commerce Management System

## Project Overview

The E-Commerce Management System is a final-year academic project developed using Python, Tkinter, and MySQL. The application provides a complete solution for managing customers, products, orders, reports, and revenue analytics through a user-friendly graphical interface.

## Technologies Used

* Python 3.x
* Tkinter (GUI)
* MySQL Database
* mysql-connector-python
* OpenPyXL
* ReportLab
* Git & GitHub

## Features

### Login Authentication

* Admin login system
* Username and password verification
* Secure access to the application

### Dashboard

* Total Customers
* Total Products
* Total Orders
* Total Revenue
* Low Stock Alerts
* Recent Orders Summary

### Customer Management

* Add Customer
* Update Customer
* Delete Customer
* Search Customer
* View Customer Records

### Product Management

* Add Product
* Update Product
* Delete Product
* Search Product
* Stock Management

### Order Management

* Select Customer
* Select Product
* Place Orders
* Automatic Total Calculation
* Automatic Stock Reduction
* Order History

### Reports

* Export Customer Report to Excel
* Export Product Report to Excel
* Export Sales Report to Excel
* Export Sales Report to PDF

## Project Structure

Ecommerce_Project

├── login.py

├── main.py

├── database.py

├── dashboard.py

├── customers.py

├── products.py

├── orders.py

├── reports.py

└── database_schema.sql

## Database Tables

### Admins

* admin_id
* username
* password

### Customers

* customer_id
* customer_name
* email
* phone
* city

### Products

* product_id
* product_name
* category
* price
* stock

### Orders

* order_id
* customer_id
* product_id
* quantity
* total_amount
* order_date

## Installation

### Install Required Packages

pip install mysql-connector-python

pip install openpyxl

pip install reportlab

### Configure Database

1. Open MySQL Workbench.
2. Execute database_schema.sql.
3. Verify that all tables are created successfully.

### Configure Database Connection

Update database.py with your MySQL credentials:

host = "localhost"

user = "root"

password = "your_password"

database = "ecommerce_db"

## Running the Project

Open Command Prompt:

cd Ecommerce_Project

python login.py

## Default Login

Username: admin

Password: admin123

## Workflow

Login

↓

Dashboard

↓

Customers

Products

Orders

Reports

↓

Logout

## Project Objectives

* Manage customer information efficiently.
* Maintain product inventory.
* Process customer orders.
* Generate reports and analytics.
* Provide a user-friendly management system.

## Future Enhancements

* Multi-user authentication
* Password encryption
* Online payment integration
* Email notifications
* Sales charts and graphs
* Cloud database integration
* Web-based deployment using Flask or Django

## Author

Naveena C J

Final Year Project

E-Commerce Management System
