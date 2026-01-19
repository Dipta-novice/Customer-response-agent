# seed_orders.py
from db import SessionLocal
from models import Order

db = SessionLocal()

db.add(Order(
    id=8847,
    customer_name="Susan Jones",
    product_ordered="KitchenPro Blender (Blue)",
    product_sent="Red Toaster",
    status="shipped"
))

db.commit()
