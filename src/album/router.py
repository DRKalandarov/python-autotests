from typing import Any
from fastapi import APIRouter, HTTPException

from src.album.schemas import AlbumRequest, AlbumResponse


router = APIRouter()


mock_data = [
    AlbumResponse(user_id=1, id=1, title="velit similique earum"),
    AlbumResponse(user_id=2, id=2, title="quo vero reiciendis"),
]


@router.get(path="/", response_model=list[AlbumResponse])
def get_albums() -> list[AlbumResponse]:
    return mock_data


@router.get(path="/{resource_id}", response_model=AlbumResponse)
def get_album_by_id(resource_id: int) -> AlbumResponse:
    for album in mock_data:
        if album["id"] == resource_id:
            return album
    raise HTTPException(status_code=404, detail="Album not found")


@router.post(path="/", response_model=AlbumResponse)
def create_album(data: AlbumRequest) -> AlbumResponse:
    return AlbumResponse(id=3, **data.model_dump())


@router.put(path="/{resource_id}", response_model=AlbumResponse)
def update_album_by_id(resource_id: int, data: AlbumRequest) -> AlbumResponse:
    return AlbumResponse(id=resource_id, **data.model_dump())


@router.delete(path="/{resource_id}")
def delete_album_by_id(resource_id: int) -> dict[str, Any]:
    return {"status": "album deleted", "id": resource_id}
