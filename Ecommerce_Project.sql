CREATE DATABASE IF NOT EXISTS ecommerce_db;

USE ecommerce_db;

DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Admins;

CREATE TABLE Admins (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

INSERT INTO Admins (username, password)
VALUES ('admin', 'admin123');

CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    city VARCHAR(50)
);

CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(100),
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id)
        REFERENCES Customers(customer_id)
        ON DELETE CASCADE,
    FOREIGN KEY (product_id)
        REFERENCES Products(product_id)
        ON DELETE CASCADE
);

INSERT INTO Customers
(customer_name,email,phone,city)
VALUES
('John','john@gmail.com','9999999999','Mysore'),
('Alex','alex@gmail.com','8888888888','Bangalore'),
('David','david@gmail.com','7777777777','Chennai');

INSERT INTO Products
(product_name,category,price,stock)
VALUES
('Laptop','Electronics',50000,20),
('Mouse','Accessories',500,50),
('Keyboard','Accessories',1500,25),
('Monitor','Electronics',12000,10),
('Printer','Office',8000,15);

INSERT INTO Orders
(customer_id,product_id,quantity,total_amount)
VALUES
(1,1,1,50000),
(2,2,2,1000),
(3,3,1,1500);