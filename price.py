from fastapi import FastAPI
import uvicorn

sinensia_api = FastAPI()


@sinensia_api.get("/")
async def root():
    return {"message": "Hola mundo"}


@sinensia_api.get("/price")
async def price():
    return {"message":  "El precio de $TSLA actualmente es: $423"}


@sinensia_api.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":

    uvicorn.run(sinensia_api, host="127.0.0.1", port=8000)