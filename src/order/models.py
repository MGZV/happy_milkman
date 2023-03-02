from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, TIMESTAMP, ForeignKey, Float, Boolean
from src.auth.models import client
from src.delivery.models import delivery
from src.product.models import product


metadata = MetaData()

order = Table(
    "order",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("added_at", TIMESTAMP, default=datetime.utcnow),
    Column("completed", Boolean, default=False, nullable=False),
    Column("client_id", Integer, ForeignKey(client.c.id)),
)

order_product = Table(
    "order_product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("added_at", TIMESTAMP, default=datetime.utcnow),
    Column("completed", Boolean, default=False, nullable=False),
    Column("count", Float),
    Column("order_id", Integer, ForeignKey(order.c.id)),
    Column("product_id", Integer, ForeignKey(product.c.id)),
    Column("delivery_id", Integer, ForeignKey(delivery.c.id)),
)


