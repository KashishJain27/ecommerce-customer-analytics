from faker import Faker
import pandas as pd
import random
import os

fake = Faker()
os.makedirs("data/raw", exist_ok=True)

customers = []
for i in range(1,1001):
    customers.append([
        f"CUST{i:04d}",
        fake.name(),
        random.choice(["Male","Female"]),
        fake.city(),
        fake.date_between(start_date="-3y", end_date="today")
    ])

customers_df = pd.DataFrame(
    customers,
    columns=[
        "customer_id",
        "customer_name",
        "gender",
        "city",
        "signup_date"
    ]
)
customers_df.to_csv("data/raw/customers.csv", index=False)
print("customers.csv created successfully!")

# -----------------------------
# Products Dataset
# -----------------------------

products = []
categories = [
    "Electronics",
    "Fashion",
    "Home Appliances",
    "Books",
    "Sports"
]

for i in range(1, 51):

    price = round(random.uniform(500, 5000), 2)

    products.append([
        f"PROD{i:03d}",
        fake.word().title(),
        random.choice(categories),
        price
    ])

products_df = pd.DataFrame(
    products,
    columns=[
        "product_id",
        "product_name",
        "category",
        "price"
    ]
)
products_df.to_csv(
    "data/raw/products.csv",
    index=False
)
print("products.csv created successfully!")

# -----------------------------
# Orders Dataset
# -----------------------------

orders = []

for i in range(1, 15001):
    quantity = random.randint(1, 5)
    price = random.uniform(500, 5000)
    sales_amount = round(quantity * price, 2)

    orders.append([
        f"ORD{i:05d}",
        f"CUST{random.randint(1,1000):04d}",
        f"PROD{random.randint(1,50):03d}",
        fake.date_between(start_date="-2y", end_date="today"),
        quantity,
        sales_amount
    ])

orders_df = pd.DataFrame(
    orders,
    columns=[
        "order_id",
        "customer_id",
        "product_id",
        "order_date",
        "quantity",
        "sales_amount"
    ]
)

orders_df.to_csv(
    "data/raw/orders.csv",
    index=False
)

print("orders.csv created successfully!")

# -----------------------------
# Payments Dataset
# -----------------------------

payments = []

payment_methods = ["UPI", "Credit Card", "Debit Card", "Net Banking", "Cash on Delivery"]
payment_statuses = ["Successful", "Failed", "Refunded"]

for i in range(1, 15001):

    payments.append([
        f"PAY{i:05d}",
        f"ORD{i:05d}",
        random.choice(payment_methods),
        random.choices(
            payment_statuses,
            weights=[85, 10, 5]
        )[0]
    ])

payments_df = pd.DataFrame(
    payments,
    columns=[
        "payment_id",
        "order_id",
        "payment_method",
        "payment_status"
    ]
)

payments_df.to_csv(
    "data/raw/payments.csv",
    index=False
)

print("payments.csv created successfully!")

# -----------------------------
# Reviews Dataset
# -----------------------------

reviews = []

for i in range(1, 8001):

    reviews.append([
        f"REV{i:05d}",
        f"CUST{random.randint(1,1000):04d}",
        f"PROD{random.randint(1,50):03d}",
        random.randint(1, 5),
        fake.date_between(start_date="-2y", end_date="today")
    ])

reviews_df = pd.DataFrame(
    reviews,
    columns=[
        "review_id",
        "customer_id",
        "product_id",
        "rating",
        "review_date"
    ]
)

reviews_df.to_csv(
    "data/raw/reviews.csv",
    index=False
)

print("reviews.csv created successfully!")

orders_cleaned = orders_df.copy()

orders_cleaned["order_date"] = pd.to_datetime(
    orders_cleaned["order_date"]
)

orders_cleaned.to_csv(
    "data/processed/orders_cleaned.csv",
    index=False
)