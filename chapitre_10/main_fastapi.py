from fastapi import FastAPI
from customer_dao import CustomerDAO

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get("/customers")
def customers():

    dao = CustomerDAO("customers.db")
    all_customers = dao.findAll()

    return list(all_customers)
