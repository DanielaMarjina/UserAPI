from fastapi import APIRouter, HTTPException

from app.models import User

from app.data import users

from app.services import (
    home_message,
    about,
    get_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
)

router = APIRouter()


@router.get("/")
def home():
    return home_message()


@router.get("/about")
def about_project():
    return about()


@router.get("/users")
def get_all_users():
    return get_users()


@router.get("/users/{user_id}")
def get_user(user_id: int):
    return get_user_by_id(user_id)


@router.post("/users", status_code=201)
def create_new_user(user: User):
    return create_user(user)


@router.put("/users/{user_id}")
def update_existing_user(user_id: int, updated_user: User):
    return update_user(user_id, updated_user)


@router.delete("/users/{user_id}")
def delete_existing_user(user_id: int):
    return delete_user(user_id)
