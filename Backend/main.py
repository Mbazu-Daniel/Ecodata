from fastapi_offline import FastAPIOffline
from fastapi import FastAPI
import uvicorn
from routes.users import user_router
from routes.blog import post_router

app = FastAPIOffline()

app.include_router(user_router)
app.include_router(post_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
