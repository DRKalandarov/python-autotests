from typing import Any
from fastapi import APIRouter

from src.comments.schemas import CommentRequest, CommentResponse


router = APIRouter()


mock_data = [
    {"postId": 1, "name": "John", "email": "test@test.com", "body": "velit similique earum", "id": 1},
    {"postId": 2, "name": "Mary", "email": "test2@test.com", "body": "quo vero reiciendis", "id": 2},
]


@router.get(path="/", response_model=list[CommentResponse])
def get_comments() -> list[dict[str, Any]]:
    return mock_data


@router.get(path="/{resource_id}", response_model=CommentResponse)
def get_comment_by_id(resource_id: int) -> dict[str, Any]:
    for data in mock_data:
        if data["id"] == resource_id:
            return data
    return {"status": "error: comment not found"}


@router.post(path="/")
def create_comment(data: CommentRequest) -> dict[str, Any]:
    data = data.model_dump()
    return {"status": "created", "data": CommentResponse(id=3, **data)}


@router.put(path="/{resource_id}")
def update_comment(resource_id: int, data: CommentRequest) -> dict[str, Any]:
    data = data.model_dump()
    return {"status": "updated", "data": CommentResponse(id=resource_id, **data)}


@router.delete(path="/{resource_id}")
def delete_comment(resource_id: int) -> dict[str, Any]:
    return {"status": "deleted", "id": id}
