from typing import Any
from fastapi import FastAPI

from schemas import CommentRequest
from schemas import CommentResponse


app = FastAPI()


mock_data = [
    {"postId": 1, "name": "John", "email": "test@test.com", "body": "velit similique earum", "id": 1},
    {"postId": 2, "name": "Mary", "email": "test2@test.com", "body": "quo vero reiciendis", "id": 2},
]


@app.get(path="/comments", response_model=list[CommentResponse])
def get_comments() -> list[CommentResponse]:
    return mock_data


@app.get(path="/comments/{id}", response_model=CommentResponse)
def get_comment_by_id(id: int) -> dict[str, Any]:
    for data in mock_data:
        if data["id"] == id:
            return data
    return {"status": "error: comment not found"}


@app.post(path="/comments")
def create_comment(data: CommentRequest) -> dict[str, Any]:
    data = data.model_dump()
    return {"status": "created", "data": CommentResponse(id=3, **data)}


@app.put(path="/comments/{id}")
def update_comment(id: int, data: CommentRequest) -> dict[str, Any]:
    data = data.model_dump()
    return {"status": "updated", "data": CommentResponse(id=id, **data)}


@app.delete(path="/comments/{id}")
def delete_comment(id: int) -> dict[str, Any]:
    return {"status": "deleted", "id": id}
