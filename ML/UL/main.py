from fastapi import FastAPI, HTTPException
app = FastAPI()
# GET request
@app.get("/")
def read_root():
    return {"message": "Welcome to Tuwaiq Academy"}
# get request
@app.get("/items/")
def create_item(item: dict):
    return {"item": item}
