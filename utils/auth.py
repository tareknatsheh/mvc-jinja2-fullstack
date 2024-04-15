
from typing import Annotated
from fastapi import Cookie
import bcrypt
import jwt
from decouple import config
import models.db as db

JWT_SECRET = config("secret")

def verify_password(stored, from_user) -> bool:
    return bcrypt.checkpw(from_user.encode('utf-8'), stored.encode('utf-8'))


def get_user(username) -> dict | None:
    all_users = db.get_data("./models/authenticated_users.json")
    if username in all_users:
        return all_users[username]
    return None

def generate_jwt_token(payload) -> str:
    token: str = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token

def verify_jwt(access_token: Annotated[str | None, Cookie()] = None):
    try:
        if access_token:
            data = jwt.decode(access_token, JWT_SECRET, algorithms=["HS256"])
            return data["role"]
        else:
            return None
    except Exception as e:
        print('error: ', e)
        print("bad token")
        return None

def validate_role(role: str | None) -> bool:
    is_loggedin = False

    if role:
        is_loggedin = True
    return is_loggedin
    