# starter-code.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, PositiveInt

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt

users = {}

@app.post("/users")
def create_user(user: User):
    if user.email in users:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    users[user.email] = user
    return user

@app.get("/users")
def list_users():
    return list(users.values())

@app.get("/users/{email}")
def get_user(email: str):
    user = users.get(email)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return user
