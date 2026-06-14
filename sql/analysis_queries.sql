-- Total Revenue
SELECT
    ROUND(SUM(sales_amount),2) AS total_revenue
FROM orders;

-- Total Customers
SELECT
    COUNT(*) AS total_customers
FROM customers;

-- Total Orders
SELECT
    COUNT(*) AS total_orders
FROM orders;

-- Average Order Value
SELECT
    ROUND(AVG(sales_amount),2) AS average_order_value
FROM orders;

-- Top 10 Customers by Revenue
SELECT
    c.customer_name,
    ROUND(SUM(o.sales_amount),2) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY revenue DESC
LIMIT 10;

-- Revenue by Category
SELECT
    p.category,
    ROUND(SUM(o.sales_amount),2) AS revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;

-- Payment Method Analysis
SELECT
    payment_method,
    COUNT(*) AS total_transactions
FROM payments
GROUP BY payment_method
ORDER BY total_transactions DESC;

-- Average Product Rating
SELECT
    p.product_name,
    ROUND(AVG(r.rating),2) AS avg_rating
FROM reviews r
JOIN products p
ON r.product_id = p.product_id
GROUP BY p.product_name
ORDER BY avg_rating DESC;