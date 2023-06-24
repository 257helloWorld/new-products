from sqlalchemy.orm import Session
from models import *
from sqlalchemy import text

# Get customer by email id
def get_user_by_email_id(db: Session, email: str):
    return db.query(Customer).filter(Customer.email == email).first()
    
# Get customer by username
def get_user_by_username(db: Session, username: str):
    return db.query(Customer).filter(Customer.username == username).first()

# Get all customers
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Customer).offset(skip).limit(limit).all()

# Create customer
def create_user(id: int, db: Session, email: str, username: str, password: str):
    db_customer = Customer(id = id, username = username, email = email, password = password)
    db.add(db_customer)
    db.commit()


# Add new Product
def add_product(db: Session, id: int, name: str, category: str, price: int):
    db_product = Product(id = id, name = name, category = category, price = price)
    db.add(db_product)
    db.commit()

# Add new Product
def buy_product(db: Session,order_id : str, customer_id: int, product_id: int, quantity: int):
    product_price = db.query(Product).filter(Product.id == product_id).one().price
    total_amount = quantity * product_price
    db_cart = Sales(order_id = order_id, customer_id = customer_id, product_id = product_id, total_amount = total_amount)
    db.add(db_cart)
    db.commit()
    return total_amount

def get_purchase_history(db: Session, username: str):
    # query = text("SELECT * FROM sales;")
    customer_id = db.query(Customer).filter(Customer.username == username).first().id
    query = text(f"SELECT sales.order_id, products.name, sales.total_amount FROM sales LEFT JOIN products ON products.id = sales.product_id WHERE customer_id = {customer_id};")
    queryResult = db.execute(query)
    print(queryResult.fetchall())
    # return history