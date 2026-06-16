from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str
    email: str

users = [
    {"id": 1, "name": "Hazem", "email": "hazem@gmail.com"},
    {"id": 2, "name": "John", "email": "john@gmail.com"},
    {"id": 3, "name": "Sara", "email": "sara@gmail.com"},
]

@app.get("/users")
def get_users():
    return users

@app.post("/users")
def add_user(user: User):
    new_user = {"id": len(users) + 1, "name": user.name, "email": user.email}
    users.append(new_user)
    return new_user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": "User deleted"}
    return {"message": "User not found"}
@app.put("/users/{user_id}")
def update_user(user_id: int, updated: User):
    for user in users:
        if user["id"] == user_id:
            user["name"] = updated.name
            user["email"] = updated.email
            return user
    return {"message": "User not found"}