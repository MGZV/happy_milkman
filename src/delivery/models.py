from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP

metadata = MetaData()

delivery = Table(
    "delivery",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("added_at", TIMESTAMP, default=datetime.utcnow),
    Column("comment", String),

)
