from fastapi_offline import FastAPIOffline
from fastapi import FastAPI
import uvicorn
from routes.api_v1.endpoints.users import user_router
from routes.api_v1.endpoints.auth import auth_router
from routes.api_v1.endpoints.blog import post_router

app = FastAPIOffline()

app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/user")
app.include_router(post_router, prefix="/post")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
