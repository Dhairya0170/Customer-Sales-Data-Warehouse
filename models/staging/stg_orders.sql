SELECT
    order_id,
    customer_id,
    order_date
FROM {{ source('public', 'orders') }}