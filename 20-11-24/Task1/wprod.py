from fastapi import FastAPI, status, HTTPException
from lprod import Logic

app = FastAPI()

@app.get("/prod/{a}")
def calculate_product(a: int, b: int):
    if a == 0 or b == 0:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail= "Input was zero"
        )
    l1 = Logic()
    result = l1.product(a, b)
    return {"message": "Success", "result": result}
