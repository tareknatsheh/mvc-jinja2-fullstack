from fastapi import FastAPI, Request
from controllers import auth, main
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# TODO
# Add a testing .json database and implement the model script --> V
# Implement authentication using bycrpt
# Authorization using jwt tokens
# Store jwt token in cookies (HttpOnly)


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(main.router, tags=["Main endpoints"])
app.include_router(auth.router, tags=["Authentication endpoints"])
    
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    print("requested url:", request.url)
    print("Exception:", exc)
    return FileResponse("./views/404.html")