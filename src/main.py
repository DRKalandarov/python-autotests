from fastapi import FastAPI

from src.comments.router import router as comments_router
from src.album.router import router as albums_router

app = FastAPI()

app.include_router(comments_router, prefix="/comments", tags=["comments"])
app.include_router(albums_router, prefix="/albums", tags=["albums"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
