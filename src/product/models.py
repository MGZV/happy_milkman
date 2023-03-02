

from sqlalchemy import MetaData, Table, Column, Integer, String, Float

metadata = MetaData()

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("count", Float),
    Column("cost", Float),
)
