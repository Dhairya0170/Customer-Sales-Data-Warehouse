SELECT
    o.order_date,
    o.customer_id,
    oi.product_id,
    oi.quantity,
    oi.quantity * p.price AS sales
FROM {{ ref('stg_orders') }} o
JOIN {{ ref('stg_order_items') }} oi
    ON o.order_id = oi.order_id
JOIN {{ ref('stg_products') }} p
    ON oi.product_id = p.product_id