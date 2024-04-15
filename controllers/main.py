from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import models.db as db

router  = APIRouter()
templates = Jinja2Templates(directory="views")

is_loggedin = True

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"is_loggedin": is_loggedin}
    )

@router.get("/store/sales")
def sales_get(request: Request):
    data = db.get_data()
    sold_items = data["items"]

    return templates.TemplateResponse(
        request=request, name="sales.html", context={"sold_items": sold_items}
    )