SELECT
    customer_id,
    customer_name,
    city,
    state,
    signup_date
FROM {{ source('public', 'customers') }}