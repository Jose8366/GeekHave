from fastapi import FastAPI
from .database import engine, Base
from .routers import users
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Serve static files from the "static" directory
app.mount("frontend/pages", StaticFiles(directory="pages"), name="pages")

# Include the router for users
app.include_router(users.router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Allow requests from this origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

class User(BaseModel):
    name: str
    email: str

# Example POST endpoint for creating a user
@app.post("/users/")
async def create_user(user: User):
    return {"message": "User created", "user": user}

# The root endpoint, serves index.html or another default file if needed
@app.get("/")
async def root():
    return FileResponse("pages/index.html")

