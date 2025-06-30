from fastapi import APIRouter, HTTPException
from app.models import Item
from app.db import db

router = APIRouter()

@router.post("/items/", response_model=Item)
def create_item(item: Item):
    if item.id in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    db[item.id] = item
    return item

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    db[item_id] = item
    return item

@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return {"message": "Item deleted"}
