from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

# Test user database
user_db = {
    "user123": "user@pswrd"
}


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


@app.get("/items/", response_model=List[Item])
async def read_items():
    return fake_items_db


@app.post("/login/")
async def login(username: str = Header(None), password: str = Header(None)):
    if username in user_db and password == user_db[username]:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Authentication failed")


@app.post("/login_create/")
async def login_create(username: str = Header(None), password: str = Header(None)):
    if username in user_db and password == user_db[username]:
        fake_items_db.append(item)
        # return item
        return {"message": "Login successful and created sucessfully..."}

    else:
        raise HTTPException(status_code=401, detail="Authentication failed")


@app.get("/v1/resource/", tags=["v1"])
async def resource_v1(api_version: str = Header(None)):
    if api_version == "1":
        return {"message": "Resource for API version 1"}
    else:
        return {"message": "API version not supported"}


@app.get("/v2/resource/", tags=["v2"])
async def resource_v2(api_version: str = Header(None)):
    if api_version == "2":
        return {"message": "Resource for API version 2"}
    else:
        return {"message": "API version not supported"}


@app.get("/greet/")
async def greet(preferred_language: str = Header(default="en")):
    greetings = {
        "en": "Hello!",
        "es": "¡Hola!",
        "fr": "Bonjour!",
        "hi": "नमस्ते!"
    }

    if preferred_language in greetings:
        return {"message": greetings[preferred_language]}
    else:
        return {"message": "Language not supported"}


if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI application on the specified host and port
    uvicorn.run(app, host="127.0.0.1", port=8000)
