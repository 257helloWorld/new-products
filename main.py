from fastapi import Depends, FastAPI, HTTPException
import models
from database import engine, get_db
from sqlalchemy.orm import Session
import crud

app = FastAPI()
models.Base.metadata.create_all(bind = engine)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/create-customer")
def create_customer(id: int, username: str, password: str, email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email_id(db, email= email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        crud.create_user(id = id, db = db, email = email, username = username, password = password)
        return "Account Created."

@app.get("/buy")
def buy(id: int,customer_id: int, product_id: int, quantity: int,db: Session = Depends(get_db)):
    total_amount = crud.buy_product(customer_id =customer_id, order_id = id, db = db, product_id = product_id, quantity=quantity)
    return f"Items worth {total_amount} bought successfully."
    

@app.get("/add-product")
def add_product(id: int, name: str, category: str, price: int, db: Session = Depends(get_db)):
    crud.add_product(id = id, name = name, category = category, db = db, price = price)
    return f"Product: {name} added successfully."

@app.get("/purchase-history")
def purchase_history(username: str, db: Session = Depends(get_db)):
    history = crud.get_purchase_history(username = username, db = db)
    return history
