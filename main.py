from fastapi import FastAPI
from database import get_connection

app = FastAPI()

@app.get("/")
def read_root():
    conn = get_connection()
    return {"status": "ok"}