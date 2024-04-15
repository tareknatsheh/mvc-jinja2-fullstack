from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/login", response_class=FileResponse)
def login_get(request: Request):
    return FileResponse("./views/login.html")

@router.post("/login")
def login_post(username: str = Form(...), password: str = Form(...)):
    if username == "tarek" and password == "t123":
        return {"message": "login successful"}
    
    raise HTTPException(status_code=401, detail="Wrong username or password")

@router.get("/logout")
def logout_get():
    return {"message": "logout successful"}
