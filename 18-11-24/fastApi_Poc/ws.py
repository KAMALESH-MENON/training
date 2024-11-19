from fastapi import FastAPI
from logic import Logic
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def test_function():
    l1 = Logic()
    return l1.rs()

@app.get("/next_num")
def wp(num):
    l1 = Logic()
    next_num = l1.get_next_integer(int(num))
    return {"result": next_num}