from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router  = APIRouter()
templates = Jinja2Templates(directory="views")

is_loggedin = True
sold_items = {
    "items": [
        {
            "date": "2024-04-14",
            "name": "ball",
            "cost": 4
        },
        {
            "date": "2024-03-10",
            "name": "phone",
            "cost": 300
        }
    ]
}

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"is_loggedin": is_loggedin}
    )

@router.get("/store/sales")
def sales_get(request: Request):
        

    return templates.TemplateResponse(
        request=request, name="sales.html", context={"sold_items": sold_items["items"]}
    )


# @router.get("/")
# def home():
#     return {"message": "You are at home page"}