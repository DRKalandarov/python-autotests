from typing import Any
from fastapi import APIRouter

from src.album.schemas import AlbumRequest, AlbumResponse


router = APIRouter()


mock_data = [
    {"userId": 1, "id": 1, "title": "velit similique earum"},
    {"userId": 2, "id": 2, "title": "quo vero reiciendis"},
]


@router.get(path="/", response_model=list[AlbumResponse])
def get_albums() -> list[dict[str, Any]]:
    return mock_data


@router.get(path="/{resource_id}", response_model=AlbumResponse)
def get_album_by_id(resource_id: int) -> dict[str, Any]:
    for data in mock_data:
        if data["id"] == resource_id:
            return data
    return {"status": "error: album not found"}


@router.post(path="/")
def create_album(data: AlbumRequest) -> dict[str, Any]:
    data = data.model_dump()
    return {"status": "created", "data": AlbumResponse(id=3, **data)}


@router.put(path="/{resource_id}")
def update_album(resource_id: int, data: AlbumRequest) -> dict[str, Any]:
    data = data.model_dump()
    return {"status": "updated", "data": AlbumResponse(id=resource_id, **data)}


@router.delete(path="/{resource_id}")
def delete_album(resource_id: int) -> dict[str, Any]:
    return {"status": "deleted", "id": resource_id}
