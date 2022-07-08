from pydantic import BaseModel


class ComicResponse(BaseModel):
    id: int
    title: str
    image: str
    onsaleDate: str


class ErrorResponse(BaseModel):
    message: str
