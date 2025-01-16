from typing import Any
from fastapi import FastAPI

from schemas import AlbumRequest
from schemas import AlbumResponse


app = FastAPI()


mock_data = [
    {"userId": 1, "id": 1, "title": "velit similique earum"},
    {"userId": 2, "id": 2, "title": "quo vero reiciendis"},
]


@app.get(path="/albums", response_model=list[AlbumResponse])
def get_albums() -> list[AlbumResponse]:
    return mock_data


@app.get(path="/albums/{id}", response_model=AlbumResponse)
def get_album_by_id(id: int) -> dict[str, Any]:
    for data in mock_data:
        if data["id"] == id:
            return data
    return {"status": "error: album not found"}


@app.post(path="/albums")
def create_album(data: AlbumRequest) -> dict[str, Any]:
    data = data.model_dump()
    return {"status": "created", "data": AlbumResponse(id=3, **data)}


@app.put(path="/albums/{id}")
def update_album(id: int, data: AlbumRequest) -> dict[str, Any]:
    data = data.model_dump()
    return {"status": "updated", "data": AlbumResponse(id=id, **data)}


@app.delete(path="/albums/{id}")
def delete_album(id: int) -> dict[str, Any]:
    return {"status": "deleted", "id": id}
