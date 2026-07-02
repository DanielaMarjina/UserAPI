from app.data import users
from app.models import User
from fastapi import HTTPException


def home_message():
    return {"message": "Hello, World!"}


def about():
    return {"language": "Python", "framework": "FastAPI"}


def get_users():
    return users


def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


def create_user(user: User):
    new_user = {"id": len(users) + 1, "name": user.name, "age": user.age}
    users.append(new_user)
    return new_user


def update_user(user_id: int, updated_user: User):
    for user in users:
        if user["id"] == user_id:
            user["name"] = updated_user.name
            user["age"] = updated_user.age
            return user

    raise HTTPException(status_code=404, detail="User not found")


def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": "User deleted"}

    raise HTTPException(status_code=404, detail="User not found")
