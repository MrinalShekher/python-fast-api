from fastapi import FastAPI
from router import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg":"Hello World"}

app.include_router(router)