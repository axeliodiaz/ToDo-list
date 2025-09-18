from fastapi import HTTPException, status

from app.core.constants import (
    HTTP_404_NOT_FOUND_DETAIL_MESSAGE,
    HTTP_401_UNAUTHORIZED_DETAIL_MESSAGE,
    HTTP_403_FORBIDDEN_DETAIL_MESSAGE,
)


class NotFoundException(HTTPException):
    def __init__(self, detail: str = HTTP_404_NOT_FOUND_DETAIL_MESSAGE):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class UnauthorizedException(HTTPException):
    def __init__(self, detail: str = HTTP_401_UNAUTHORIZED_DETAIL_MESSAGE):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


class ForbiddenException(HTTPException):
    def __init__(self, detail: str = HTTP_403_FORBIDDEN_DETAIL_MESSAGE):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)
