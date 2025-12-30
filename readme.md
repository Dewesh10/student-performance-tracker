# Student Performance Tracker

## Objective
To design and implement a full-stack data-driven dashboard using REST APIs,
MongoDB database, and interactive visualization.

## Technology Stack
- Backend: FastAPI (Python)
- Database: MongoDB (NoSQL)
- Frontend Dashboard: Plotly Dash
- Dataset: CSV (50+ records)

## Features
- CRUD operations via REST APIs
- MongoDB document-based storage
- Interactive dashboard with bar, pie, and scatter charts
- Real-time data reflection

## How to Run
1. Start MongoDB server
2. Run backend:
   uvicorn main:app --reload
3. Load data:
   python load_csv.py
4. Run dashboard:
   python dashboard.py

## API Endpoints
- GET /students
- POST /students
- PUT /students/{id}
- DELETE /students/{id}

## How to Run This Project

1. Clone the repository or download ZIP
2. Ensure MongoDB is running locally
3. Install dependencies:
   pip install fastapi uvicorn pymongo dash pandas plotly requests
4. Load sample data:
   python load_csv.py
5. Start backend server:
   uvicorn main:app --reload
6. Start dashboard (new terminal):
   python dashboard.py

Backend: http://127.0.0.1:8000/docs  
Dashboard: http://127.0.0.1:8050
