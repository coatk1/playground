# Source: https://fastapi.tiangolo.com/tutorial/

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def main():
    # return {"message": "Hello World"}
    content = """
    <body>
        <h1>Test</h1>
    </body>
    """
    return HTMLResponse(content=content)


@app.get("/api")
async def root():
    return {"message": "Hello World"}


@app.get("/dummy")
async def dummy():
    return {"message": "Educated Dummies"}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
