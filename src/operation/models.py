from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Float
from src.order.models import order

metadata = MetaData()

operation_category = Table(
    "operation_category",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("added_at", TIMESTAMP, default=datetime.utcnow),
    Column("amount", Float),
    Column("order_id", Integer, ForeignKey(order.c.id)),
    Column("operation_category_id", Integer, ForeignKey(operation_category.c.id)),
)
