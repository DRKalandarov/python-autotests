from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class Album(BaseModel):
    user_id: int | None = Field(default=None)
    id: int
    title: str | None = Field(default=None)

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
