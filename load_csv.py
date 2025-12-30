import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]
collection = db["students"]

df = pd.read_csv("students_50.csv")
collection.insert_many(df.to_dict("records"))

print("✅ 50 students inserted successfully")
