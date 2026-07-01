from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, World!"}


@app.get("/about")
def about():
    return {"language": "Python", "framework": "FastAPI"}


@app.get("/name")
def get_name():
    return {"name": "Daniela"}


users = [
    {"id": 1, "name": "Ana", "age": 19},
    {"id": 2, "name": "Ion", "age": 17},
    {"id": 3, "name": "Maria", "age": 22},
]


@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


class User(BaseModel):
    name: str
    age: int


@app.post("/users", status_code=201)
def create_user(user: User):
    new_user = {"id": len(users) + 1, "name": user.name, "age": user.age}
    users.append(new_user)
    return new_user


@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for user in users:
        if user["id"] == user_id:
            user["name"] = updated_user.name
            user["age"] = updated_user.age
            return user

    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": "User deleted"}

    raise HTTPException(status_code=404, detail="User not found")
