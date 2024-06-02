from fastapi import FastAPI

app = FastAPI()

@app.get("/tes")
def test():
    return "Hello, World!"
