from typing import Any
from fastapi import APIRouter, HTTPException

from src.comments.schemas import CommentRequest, CommentResponse


router = APIRouter()


mock_data = [
    CommentResponse(post_id=1, name="John", email="test@test.com", body="velit similique earum", id=1),
    CommentResponse(post_id=2, name="Mary", email="test2@test.com", body="quo vero reiciendis", id=2),
]


@router.get(path="/", response_model=list[CommentResponse])
def get_comments() -> list[CommentResponse]:
    return mock_data


@router.get(path="/{resource_id}", response_model=CommentResponse)
def get_comment_by_id(resource_id: int) -> CommentResponse:
    for comment in mock_data:
        if comment["id"] == resource_id:
            return comment
    raise HTTPException(status_code=404, detail="Comment not found")


@router.post(path="/", response_model=CommentResponse)
def create_comment(data: CommentRequest) -> CommentResponse:
    return CommentResponse(id=3, **data.model_dump())


@router.put(path="/{resource_id}", response_model=CommentResponse)
def update_comment_by_id(resource_id: int, data: CommentRequest) -> CommentResponse:
    return CommentResponse(id=resource_id, **data.model_dump())


@router.delete(path="/{resource_id}")
def delete_comment_by_id(resource_id: int) -> dict[str, Any]:
    return {"status": "comment deleted", "id": resource_id}
