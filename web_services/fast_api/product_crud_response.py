from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Model for Item


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


# Fake database to store items
fake_items_db = []

# Create operation


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    fake_items_db.append(item)
    return item

# Read operation


@app.get("/items/", response_model=List[Item])
async def read_items():
    return fake_items_db

# Update operation


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    if item_id < 0 or item_id >= len(fake_items_db):
        raise HTTPException(status_code=404, detail="Item not found")

    fake_items_db[item_id] = updated_item
    return updated_item

# Delete operation


@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_items_db):
        raise HTTPException(status_code=404, detail="Item not found")

    deleted_item = fake_items_db.pop(item_id)
    return deleted_item


app = FastAPI()

# Model for Item


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


# Fake database to store items
fake_items_db = []

# Create operation


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    fake_items_db.append(item)
    return item

# Read operation


@app.get("/items/", response_model=List[Item])
async def read_items():
    return fake_items_db

# Update operation


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    if item_id < 0 or item_id >= len(fake_items_db):
        raise HTTPException(status_code=404, detail="Item not found")

    fake_items_db[item_id] = updated_item
    return updated_item

# Delete operation


@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_items_db):
        raise HTTPException(status_code=404, detail="Item not found")

    deleted_item = fake_items_db.pop(item_id)
    return deleted_item

if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI application on the specified
    uvicorn.run(app, host="127.0.0.1", port=8000)
