from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, mapped_column
from database import Base

# Tables

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    username = Column(String, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String)

    def __repr__(self):
        return f"<Customer self.username>"

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    price = Column(Integer)

class Sales(Base):
    __tablename__ = "sales"

    order_id = Column(Integer, primary_key=True)
    customer_id = mapped_column(ForeignKey('customers.id'))
    product_id = mapped_column(ForeignKey('products.id'))
    total_amount = Column(Integer)