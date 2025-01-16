from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class AlbumBase(BaseModel):
    user_id: int | None = Field(default=None)
    title: str | None = Field(default=None)

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True, extra="forbid")


class AlbumRequest(AlbumBase):
    pass


class AlbumResponse(AlbumBase):
    id: int
