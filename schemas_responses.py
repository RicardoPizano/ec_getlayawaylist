from models.responses import ComicResponse, ErrorResponse

add_to_layaway_response = {
    200: {"model": ComicResponse},
    409: {"model": ErrorResponse}
}
