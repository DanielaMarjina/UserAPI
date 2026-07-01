from fastapi import APIRouter, HTTPException

from app.models import User

from app.data import users

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Hello, World!"}


@router.get("/about")
def about():
    return {"language": "Python", "framework": "FastAPI"}


@router.get("/name")
def get_name():
    return {"name": "Daniela"}


@router.get("/users")
def get_users():
    return users


@router.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.post("/users", status_code=201)
def create_user(user: User):
    new_user = {"id": len(users) + 1, "name": user.name, "age": user.age}
    users.append(new_user)
    return new_user


@router.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for user in users:
        if user["id"] == user_id:
            user["name"] = updated_user.name
            user["age"] = updated_user.age
            return user

    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": "User deleted"}

    raise HTTPException(status_code=404, detail="User not found")
