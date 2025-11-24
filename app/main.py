import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.config import TORTOISE_ORM

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


register_tortoise(
    app,
    db_url=TORTOISE_ORM['connections']['default'],
    modules={"models": []},
    generate_schemas=False,
    add_exception_handlers=True,
)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False, workers=1)
