-- Load Customer Dimension
INSERT INTO dim_customers (customer_id, customer_name, city, state)
SELECT
    customer_id,
    customer_name,
    city,
    state
FROM customers;

-- Load Product Dimension
INSERT INTO dim_products (product_id, product_name, category, price)
SELECT
    product_id,
    product_name,
    category,
    price
FROM products;

-- Load Date Dimension
INSERT INTO dim_date (date_key, year, quarter, month, day)
SELECT DISTINCT
    order_date,
    EXTRACT(YEAR FROM order_date),
    EXTRACT(QUARTER FROM order_date),
    EXTRACT(MONTH FROM order_date),
    EXTRACT(DAY FROM order_date)
FROM orders;