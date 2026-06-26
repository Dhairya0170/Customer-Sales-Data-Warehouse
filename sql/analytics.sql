INSERT INTO fact_orders (
    date_key,
    customer_key,
    product_key,
    quantity,
    sales
)
SELECT
    o.order_date,
    dc.customer_key,
    dp.product_key,
    oi.quantity,
    oi.quantity * dp.price
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
JOIN dim_customers dc
    ON dc.customer_id = o.customer_id
JOIN dim_products dp
    ON dp.product_id = oi.product_id;