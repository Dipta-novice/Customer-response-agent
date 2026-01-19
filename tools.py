from langchain.tools import tool
from db import SessionLocal
from models import Order

@tool
def orders_database_query(order_id: int) -> dict:
    """Fetch order details by order ID"""
    db = SessionLocal()
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        return {"error": "Order not found"}

    return {
        "order_id": order.id,
        "customer": order.customer_name,
        "ordered": order.product_ordered,
        "sent": order.product_sent,
        "status": order.status,
    }

@tool
def request_review(draft_response: str) -> str:
    """Send draft response for human review"""
    # Later: Slack, Email, Jira, etc.
    return f"REVIEW REQUESTED:\n{draft_response}"
