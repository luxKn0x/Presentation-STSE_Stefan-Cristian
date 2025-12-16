import random
import time
import requests
from datetime import datetime

ELASTIC_URL = "https://my-elasticsearch-project-cfbc16.es.us-central1.gcp.elastic.cloud:443"
API_KEY = "T3NDcEdac0I5ZURwWnFvd1FELWQ6RjZXT3h2WlBNenk3ZEVNaFdrSTFNdw=="

INDEX_NAME = "ecommerce-sales"

headers = {
    "Authorization": f"ApiKey {API_KEY}",
    "Content-Type": "application/json"
}

product_catalog = [
    {"name": "Laptop", "category": "Electronics", "price": 4500},
    {"name": "Smartphone", "category": "Electronics", "price": 2800},
    {"name": "Headphones", "category": "Electronics", "price": 450},
    {"name": "T-shirt", "category": "Clothing", "price": 120},
    {"name": "Jeans", "category": "Clothing", "price": 250},
    {"name": "Sneakers", "category": "Clothing", "price": 480},
    {"name": "Coffee Machine", "category": "Home Appliances", "price": 900},
    {"name": "Vacuum Cleaner", "category": "Home Appliances", "price": 1100},
    {"name": "Book", "category": "Books", "price": 80},
    {"name": "Backpack", "category": "Accessories", "price": 200},
]

countries = ["Romania", "Germany", "France", "UK", "Italy"]
cities = ["Bucharest", "Berlin", "Paris", "London", "Rome"]
payment_methods = ["Card", "Cash on Delivery", "PayPal"]
order_statuses = ["Completed", "Pending", "Cancelled"]

def generate_sale():
    product = random.choice(product_catalog)
    quantity = random.randint(1, 4)
    total_price = product["price"] * quantity

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "order_id": random.randint(100000, 999999),
        "product_name": product["name"],
        "category": product["category"],
        "unit_price": product["price"],
        "quantity": quantity,
        "total_price": total_price,
        "payment_method": random.choice(payment_methods),
        "order_status": random.choices(
            order_statuses, weights=[0.8, 0.15, 0.05]
        )[0],
        "buyer": {
            "buyer_id": random.randint(1, 1000),
            "age": random.randint(18, 70),
            "country": random.choice(countries),
            "city": random.choice(cities),
        },
        "delivery_address": {
            "street": f"Street {random.randint(1, 100)}",
            "city": random.choice(cities),
            "country": random.choice(countries),
            "postal_code": f"{random.randint(10000,99999)}"
        }
    }

while True:
    sale = generate_sale()

    response = requests.post(
        f"{ELASTIC_URL}/{INDEX_NAME}/_doc",
        headers=headers,
        json=sale
    )

    print("Sent sale:", sale)
    time.sleep(3)