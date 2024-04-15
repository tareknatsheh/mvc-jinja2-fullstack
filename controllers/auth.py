from re import template
from typing import Annotated
from fastapi import APIRouter, HTTPException, Request, Form, Response, status
from fastapi.responses import FileResponse, RedirectResponse

import utils.auth as auth

router = APIRouter()

@router.get("/login", response_class=FileResponse)
def login_get(request: Request):
    """Renders the login html page

    Args:
        request (Request)

    Returns:
        login form (html)
    """
    return FileResponse("./views/login.html")

@router.post("/login")
def login_post(request: Request, response: Response, username: str = Form(...), password: str = Form(...)):
    """handles the login post request by the login form

    Args:
        username (str, required)
        password (str, required)

    Raises:
        HTTPException: if login credintials are wrong

    Returns:
        _type_: _description_
    """

    user = auth.get_user(username)

    if user:
        stored_password = user["password"]
        is_password_correct = auth.verify_password(stored_password, password)
        if not is_password_correct:
            raise HTTPException(status_code=401, detail="Wrong username or password")

        token: str = auth.generate_jwt_token({"role": "user"})

        redirect_url = request.url_for('home') 
        resp =  RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
        resp.set_cookie(key="access_token",value=f"{token}", httponly=True)

        return resp

    else:
        raise HTTPException(status_code=401, detail="Wrong username or password")


@router.get("/logout")
def logout_get(request: Request):
    """Log the user out by deleting their jwt access_token cookie

    Args:
        request (Request)


    Redirect: to home page /
    
    """
    redirect_url = request.url_for('home') 
    resp =  RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    resp.delete_cookie(key="access_token")

    return resp
