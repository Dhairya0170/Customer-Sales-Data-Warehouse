from pathlib import Path
from faker import Faker
import pandas as pd
import random

# -----------------------------
# Setup
# -----------------------------
fake = Faker()

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

# ==================================================
# Generate Customers
# ==================================================

customers = []

for _ in range(5000):
    customers.append({
        "customer_name": fake.name(),
        "city": fake.city(),
        "state": fake.state(),
        "signup_date": fake.date_between(start_date="-3y", end_date="today")
    })

customer_df = pd.DataFrame(customers)

customer_df.to_csv(RAW_DATA_DIR / "customers.csv", index=False)

print("✅ customers.csv created")

# ==================================================
# Generate Products
# ==================================================

product_catalog = {
    "Laptop": {
        "brands": ["Dell", "HP", "Lenovo", "Apple", "Asus"],
        "models": ["Pro", "Air", "Elite", "ThinkBook", "XPS", "ZenBook"],
        "price": (45000, 150000)
    },

    "Smartphone": {
        "brands": ["Apple", "Samsung", "OnePlus", "Google", "Xiaomi"],
        "models": ["Ultra", "Pro", "Plus", "Max", "Lite"],
        "price": (12000, 90000)
    },

    "Headphones": {
        "brands": ["Sony", "Boat", "JBL", "Noise", "Bose"],
        "models": ["X100", "Pro", "Max", "Elite"],
        "price": (1000, 25000)
    },

    "Keyboard": {
        "brands": ["Logitech", "HP", "Redragon", "Corsair"],
        "models": ["K100", "MK270", "RGB", "Wireless"],
        "price": (800, 9000)
    },

    "Mouse": {
        "brands": ["Logitech", "HP", "Dell", "Razer"],
        "models": ["M185", "G502", "Pro", "Wireless"],
        "price": (500, 7000)
    },

    "Monitor": {
        "brands": ["Samsung", "LG", "Dell", "BenQ"],
        "models": ["24\"", "27\"", "32\"", "Curved"],
        "price": (7000, 45000)
    }
}

products = []

for _ in range(300):

    category = random.choice(list(product_catalog.keys()))

    brand = random.choice(product_catalog[category]["brands"])

    model = random.choice(product_catalog[category]["models"])

    price_range = product_catalog[category]["price"]

    price = random.randint(price_range[0], price_range[1])

    products.append({
        "product_name": f"{brand} {model}",
        "category": category,
        "price": price
    })

product_df = pd.DataFrame(products)

product_df.to_csv(RAW_DATA_DIR / "products.csv", index=False)

print("✅ products.csv created")

# ==================================================
# Generate Orders
# ==================================================

orders = []

order_id = 1

for customer_id in range(1, len(customer_df) + 1):

    num_orders = random.randint(1, 8)

    for _ in range(num_orders):

        orders.append({
            "order_id": order_id,
            "customer_id": customer_id,
            "order_date": fake.date_between(
                start_date="-2y",
                end_date="today"
            )
        })

        order_id += 1

order_df = pd.DataFrame(orders)

order_df.to_csv(
    RAW_DATA_DIR / "orders.csv",
    index=False
)

print("✅ orders.csv created")

# ==================================================
# Generate Order Items
# ==================================================

# ==================================================
# Generate Order Items
# ==================================================

order_items = []

order_item_id = 1

for order in order_df.itertuples():
    # Each order contains 1 to 5 different products
    num_products = random.randint(1, 5)

    for _ in range(num_products):
        product_id = random.randint(1, len(product_df))
        quantity = random.randint(1, 4)

        order_items.append({
            "order_item_id": order_item_id,
            "order_id": order.order_id,
            "product_id": product_id,
            "quantity": quantity
        })

        order_item_id += 1

# Convert to DataFrame
order_items_df = pd.DataFrame(order_items)

# Save CSV
order_items_df.to_csv(
    RAW_DATA_DIR / "order_items.csv",
    index=False
)

print("✅ order_items.csv created")