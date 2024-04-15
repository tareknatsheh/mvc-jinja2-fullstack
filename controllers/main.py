from typing import Annotated
from fastapi import APIRouter, Request, Depends, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import models.db as db
import utils.auth as auth

router  = APIRouter()
templates = Jinja2Templates(directory="views")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request, role: Annotated[str | None, Depends(auth.verify_jwt)]):
    print("ROLE is", role)
    
    is_loggedin = auth.validate_role(role)

    return templates.TemplateResponse(
        request=request, name="index.html", context={"is_loggedin": is_loggedin}
    )

@router.get("/store/sales")
def sales_get(request: Request, role: Annotated[str | None, Depends(auth.verify_jwt)]):
    
    is_loggedin = auth.validate_role(role)

    if not is_loggedin:
        redirect_url = request.url_for('home') 
        return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
    
    data = db.get_data("./models/data.json")
    sold_items = data["items"]

    return templates.TemplateResponse(
        request=request, name="sales.html", context={"sold_items": sold_items}
    )
