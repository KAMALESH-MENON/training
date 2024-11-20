from fastapi import FastAPI
from pydantic import BaseModel
from logic import Logic

# Create a Pydantic model for the input (Rectangle)
class Product(BaseModel):
    id: int
    name: str
    price: float

# Initialize FastAPI app
app = FastAPI()

@app.post("/add_product")
async def add_product(new_product: Product):
    l1 = Logic()
    result = l1.add_product(new_product)
    return result

@app.get("/get_product")
async def get_product():
    l1 = Logic()
    result = l1.list_products()
    return result

@app.put("/update_product")
async def update_product(update_product: Product):
    l1 = Logic()
    result = l1.update_product(update_product)
    return result

@app.put("/apply_discount")
async def apply_discount(discount_percentage: int):
    l1 = Logic()
    result = l1.apply_discount(discount_percentage)
    return result
