from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.chat_routes import router
from database import init_db

app = FastAPI()

# Allow React frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your React URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB
init_db()

# Include chat routes
app.include_router(router)