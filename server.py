from fastapi import FastAPI, Request
from controllers import auth, main
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# TODO
# Add a testing .json database and implement the model script --> done
# Implement authentication using bycrpt --> done
# Authorization using jwt tokens --> done
# Store jwt token in cookies (HttpOnly?) --> done
# Write the README.md --> done
# Write tests for:
# - login flow --> done
# - logout flow --> done
# - sales page flow
# Create CI pipeline using Github Actions
# List sales items in a Table not a list


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(main.router, tags=["Main endpoints"])
app.include_router(auth.router, tags=["Authentication endpoints"])
    
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    print("requested url:", request.url)
    print("Exception:", exc)
    return FileResponse("./views/404.html")


def playground():
    import requests
    res = requests.get("http://127.0.0.1:8000/logout")

    print(res.text)
    print(res.headers)
    

if __name__ == "__main__":
    playground()