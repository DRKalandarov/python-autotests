from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class Comment(BaseModel):
    post_id: int | None = Field(default=None)
    name: str | None = Field(default=None)
    email: str | None = Field(default=None)
    body: str | None = Field(default=None)

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
