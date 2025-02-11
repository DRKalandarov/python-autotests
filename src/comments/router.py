from typing import Any
from fastapi import FastAPI

from schemas import CommentRequest, CommentResponse


app = FastAPI()


mock_data = [
    {"postId": 1, "name": "John", "email": "test@test.com", "body": "velit similique earum", "id": 1},
    {"postId": 2, "name": "Mary", "email": "test2@test.com", "body": "quo vero reiciendis", "id": 2},
]


@app.get(path="/comments", response_model=list[CommentResponse])
def get_comments() -> list[dict[str, Any]]:
    return mock_data


@app.get(path="/comments/{resource_id}", response_model=CommentResponse)
def get_comment_by_id(resource_id: int) -> dict[str, Any]:
    for data in mock_data:
        if data["id"] == resource_id:
            return data
    return {"status": "error: comment not found"}


@app.post(path="/comments")
def create_comment(data: CommentRequest) -> dict[str, Any]:
    data = data.model_dump()
    return {"status": "created", "data": CommentResponse(id=3, **data)}


@app.put(path="/comments/{resource_id}")
def update_comment(resource_id: int, data: CommentRequest) -> dict[str, Any]:
    data = data.model_dump()
    return {"status": "updated", "data": CommentResponse(id=resource_id, **data)}


@app.delete(path="/comments/{resource_id}")
def delete_comment(resource_id: int) -> dict[str, Any]:
    return {"status": "deleted", "id": id}
