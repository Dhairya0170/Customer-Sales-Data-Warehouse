SELECT
    order_item_id,
    order_id,
    product_id,
    quantity
FROM {{ source('public', 'order_items') }}