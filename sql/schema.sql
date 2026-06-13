CREATE DATABASE IF NOT EXISTS ecommerce_customer_analytics;

USE ecommerce_customer_analytics;

CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100),
    gender VARCHAR(10),
    city VARCHAR(100),
    signup_date DATE
);

CREATE TABLE products (
    product_id VARCHAR(10) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    product_id VARCHAR(10),
    order_date DATE,
    quantity INT,
    sales_amount DECIMAL(10,2),

    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id),

    FOREIGN KEY (product_id)
    REFERENCES products(product_id)
);

CREATE TABLE payments (
    payment_id VARCHAR(10) PRIMARY KEY,
    order_id VARCHAR(10),
    payment_method VARCHAR(50),
    payment_status VARCHAR(50),

    FOREIGN KEY (order_id)
    REFERENCES orders(order_id)
);

CREATE TABLE reviews (
    review_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    product_id VARCHAR(10),
    rating INT,
    review_date DATE,

    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id),

    FOREIGN KEY (product_id)
    REFERENCES products(product_id)
);
