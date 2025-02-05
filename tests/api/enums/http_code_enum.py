from enum import Enum


class HttpCodeEnum(Enum):
    OK = 200
    CREATED = 201
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
