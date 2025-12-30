from fastapi import FastAPI
from api import router

app = FastAPI(title="Student Performance Tracker API")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Student Performance Tracker API Running"}
