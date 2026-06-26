SELECT
    product_id,
    product_name,
    category,
    price
FROM {{ source('public', 'products') }}