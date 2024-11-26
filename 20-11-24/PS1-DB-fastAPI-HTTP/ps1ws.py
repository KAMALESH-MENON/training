from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from logic import Logic

# Create a Pydantic model for the input (Rectangle)
class Product(BaseModel):
    id: int
    name: str
    price: float

# Initialize FastAPI app
app = FastAPI()
l1 = Logic()

@app.post("/add_product", status_code=status.HTTP_201_CREATED)
async def add_product(new_product: Product):
    result = l1.add_product(new_product)
    if result is False:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail= "Product not added."
        )
    return result

@app.get("/get_product")
async def get_product(status_code=status.HTTP_200_OK):
    result = l1.list_products()
    if len(result) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Empty list products"
        )
    return result

@app.put("/update_product")
async def update_product(update_product: Product, status_code=status.HTTP_200_OK):
    result = l1.update_product(update_product)
    if result is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Product not found."
        )
    return result

@app.put("/apply_discount")
async def apply_discount(discount_percentage: int, status_code=status.HTTP_200_OK):
    if discount_percentage<=0 or discount_percentage>=100:
        raise HTTPException(
            status_code=status.HTTP_ ,
            detail= "Product not found."
        )
    result = l1.apply_discount(discount_percentage)
    return result
