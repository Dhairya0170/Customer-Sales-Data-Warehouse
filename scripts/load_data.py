import pandas as pd
from pathlib import Path
import psycopg2

# -----------------------------
# Project Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

# -----------------------------
# Connect to PostgreSQL
# -----------------------------
connection = psycopg2.connect(
    host="localhost",
    database="customer_sales_dw",
    user="postgres",
    password="1234"
)

cursor = connection.cursor()

print("✅ Connected to PostgreSQL")


# -----------------------------
# Load Customers
# -----------------------------
def load_customers():
    customer_df = pd.read_csv(RAW_DATA_DIR / "customers.csv")

    for row in customer_df.itertuples(index=False):
        cursor.execute(
            """
            INSERT INTO customers
            (customer_name, city, state, signup_date)
            VALUES (%s,%s,%s,%s)
            """,
            (
                row.customer_name,
                row.city,
                row.state,
                row.signup_date
            )
        )

    connection.commit()
    print(f"✅ Loaded {len(customer_df)} customers")


# -----------------------------
# Load Products
# -----------------------------
def load_products():
    product_df = pd.read_csv(RAW_DATA_DIR / "products.csv")

    for row in product_df.itertuples(index=False):
        cursor.execute(
            """
            INSERT INTO products
            (product_name, category, price)
            VALUES (%s,%s,%s)
            """,
            (
                row.product_name,
                row.category,
                row.price
            )
        )

    connection.commit()
    print(f"✅ Loaded {len(product_df)} products")


# -----------------------------
# Load Orders
# -----------------------------
def load_orders():
    order_df = pd.read_csv(RAW_DATA_DIR / "orders.csv")

    for row in order_df.itertuples(index=False):
        cursor.execute(
            """
            INSERT INTO orders
            (order_id, customer_id, order_date)
            VALUES (%s,%s,%s)
            """,
            (
                row.order_id,
                row.customer_id,
                row.order_date
            )
        )

    connection.commit()
    print(f"✅ Loaded {len(order_df)} orders")


# -----------------------------
# Load Order Items
# -----------------------------
def load_order_items():
    order_items_df = pd.read_csv(RAW_DATA_DIR / "order_items.csv")

    for row in order_items_df.itertuples(index=False):
        cursor.execute(
            """
            INSERT INTO order_items
            (order_item_id, order_id, product_id, quantity)
            VALUES (%s,%s,%s,%s)
            """,
            (
                row.order_item_id,
                row.order_id,
                row.product_id,
                row.quantity
            )
        )

    connection.commit()
    print(f"✅ Loaded {len(order_items_df)} order items")


# -----------------------------
# Run ETL
# -----------------------------
load_customers()
load_products()
load_orders()
load_order_items()

# -----------------------------
# Close Connection
# -----------------------------
cursor.close()
connection.close()

print("✅ ETL Completed Successfully")