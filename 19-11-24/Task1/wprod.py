from fastapi import FastAPI
from lprod import Logic

app = FastAPI()

@app.get("/prod/{a}")
def calculate_product(a: int, b: int):
    if a == 0 or b == 0:
        return {"message": "Input was zero"}
    l1 = Logic()
    result = l1.product(a, b)
    return {"message": "Success", "result": result}