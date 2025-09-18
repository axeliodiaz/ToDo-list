from fastapi import HTTPException

from app.core.constants import TODO_404_NOT_FOUND_DETAIL_MESSAGE


TODO_404_NOT_FOUND = HTTPException(
    status_code=404, detail=TODO_404_NOT_FOUND_DETAIL_MESSAGE
)
