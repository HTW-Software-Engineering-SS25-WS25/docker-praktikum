from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import Dict, List, Optional
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*",  # Allows all origins
]

app = FastAPI(title="Users API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods)
)

# Pydantic models for request validation and documentation


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserPartialUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None


class User(UserBase):
    id: int

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "name": "Alice",
                "email": "alice@example.com"
            }
        }
    }


# In-memory database
users: Dict[int, Dict] = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
}
next_id = 3

# GET all users


@app.get("/", tags=["root"], summary="Root endpoint")
def read_root():
    """
    Root endpoint to check if the API is running
    """
    return {
        "version": "1.0",
        "description": "Users API",
        "documentation": "Visit /docs for Swagger UI or /redoc for ReDoc"
    }


@app.get("/users", response_model=List[User], tags=["users"], summary="Get all users")
def get_users():
    """
    Retrieve a list of all users in the system
    """
    return list(users.values())

# GET a specific user


@app.get("/users/{user_id}", response_model=User, tags=["users"], summary="Get user by ID")
def get_user(user_id: int):
    """
    Retrieve a specific user by their ID
    """
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

# POST - Create a new user


@app.post("/users", response_model=User, status_code=201, tags=["users"], summary="Create a new user")
def create_user(user: UserCreate):
    """
    Create a new user with the provided name and email
    """
    global next_id
    new_user = {
        "id": next_id,
        "name": user.name,
        "email": user.email
    }
    users[next_id] = new_user
    next_id += 1
    return new_user

# PUT - Update a user completely


@app.put("/users/{user_id}", response_model=User, tags=["users"], summary="Update a user")
def update_user(user_id: int, user: UserUpdate):
    """
    Update all fields of an existing user
    """
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    users[user_id] = {
        "id": user_id,
        "name": user.name,
        "email": user.email
    }
    return users[user_id]

# PATCH - Update parts of a user


@app.patch("/users/{user_id}", response_model=User, tags=["users"], summary="Partially update a user")
def partial_update_user(user_id: int, user: UserPartialUpdate):
    """
    Update one or more fields of an existing user
    """
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    stored_user = users[user_id]

    if user.name is not None:
        stored_user["name"] = user.name
    if user.email is not None:
        stored_user["email"] = user.email

    return stored_user

# DELETE - Remove a user


@app.delete("/users/{user_id}", tags=["users"], summary="Delete a user")
def delete_user(user_id: int):
    """
    Delete a user from the system
    """
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    deleted_user = users.pop(user_id)
    return {"message": f"User {deleted_user['name']} deleted successfully"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
