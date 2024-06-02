from fastapi import FastAPI

from app.api.api_v1 import api_router

app = FastAPI(
    title="Explinability of the exercise performance",
    description="This is the API to perform explainability of the exercise performance",
    version="0.1.0",
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def test():
    return {"message": "Hello!"}
