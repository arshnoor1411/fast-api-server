from typing import Union

from fastapi import FastAPI

from src.user.signup import router as user_router

app = FastAPI()

app.include_router(user_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}