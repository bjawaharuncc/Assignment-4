from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# create the FastAPI app instance
app = FastAPI(title="Assignment 4 - FastAPI Implementation")

# model for PUT request body
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

# root endpoint - shows server is running
@app.get("/")
def root():
    return {"message": "FastAPI Assignment 4 running"}

# simple get endpoint with path + query params
@app.get("/items/{item_id}")
def get_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "query": q}

# put endpoint for updating an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"updated_id": item_id, "data": item}
