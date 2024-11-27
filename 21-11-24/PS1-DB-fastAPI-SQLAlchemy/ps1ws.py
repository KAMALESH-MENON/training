from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from logic import Logic
from product import Product as ProductModel
from sqlalchemy.orm import Session
from config import get_db
from config import engine, Base

app = FastAPI()
l1 = Logic()

Base.metadata.create_all(bind=engine)

class Product(BaseModel):
    id: int
    name: str
    price: float

@app.post("/add_product")
async def add_product(new_product: Product):
    product_model = ProductModel(id=new_product.id, name=new_product.name, price=new_product.price)
    result = l1.add_product(product_model)
    if not result:
        raise HTTPException(status_code=400, detail="Product could not be added")
    return {"message": "Product added successfully"}

@app.get("/get_product")
async def get_product():
    result = l1.list_products()
    return result

@app.put("/update_product")
async def update_product(update_product: Product):
    product_model = ProductModel(id=update_product.id, name=update_product.name, price=update_product.price)
    result = l1.update_product(product_model)
    if not result:
        raise HTTPException(status_code=400, detail="Product could not be updated")
    return {"message": "Product updated successfully"}

@app.put("/apply_discount")
async def apply_discount(discount_percentage: int):
    result = l1.apply_discount(discount_percentage)
    return result
