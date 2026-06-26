CREATE TABLE dim_customers (

    customer_key SERIAL PRIMARY KEY,
    customer_id INT UNIQUE,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50)

);

CREATE TABLE dim_products (

    product_key SERIAL PRIMARY KEY,
    product_id INT UNIQUE,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10,2)

);

CREATE TABLE dim_date (

    date_key DATE PRIMARY KEY,
    year INT,
    quarter INT,
    month INT,
    day INT

);

CREATE TABLE fact_orders (

    fact_order_key SERIAL PRIMARY KEY,
    date_key DATE REFERENCES dim_date(date_key),
    customer_key INT REFERENCES dim_customers(customer_key),
    product_key INT REFERENCES dim_products(product_key),
    quantity INT,
    sales NUMERIC(10,2)

);