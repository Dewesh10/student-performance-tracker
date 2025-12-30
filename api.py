from fastapi import APIRouter
from bson import ObjectId
from database import collection

router = APIRouter()

def serialize(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@router.post("/students")
def add_student(student: dict):
    collection.insert_one(student)
    return {"message": "Student added"}

@router.get("/students")
def get_students():
    return [serialize(s) for s in collection.find()]

@router.put("/students/{id}")
def update_student(id: str, data: dict):
    collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return {"message": "Student updated"}

@router.delete("/students/{id}")
def delete_student(id: str):
    collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Student deleted"}
