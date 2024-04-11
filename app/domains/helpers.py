from http import HTTPStatus

from fastapi import HTTPException


def raise_not_found_error(query, message):
    if not query:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=message
        )
