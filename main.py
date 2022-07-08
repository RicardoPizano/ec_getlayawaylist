from typing import Union

import pymongo
from fastapi import FastAPI, Response, Header, status

import logger
from auth import auth
from constans import MONGO_URL
from models.enums import OrderByEnum
from models.responses import ErrorResponse, ComicResponse
from repositories import db
from schemas_responses import add_to_layaway_response

app = FastAPI()

LOGGER_FILE_NAME = "main.py"

client = pymongo.MongoClient(MONGO_URL)
db_session = client.ecdb_comics


@app.get("/getLayawayList", responses={**add_to_layaway_response})
async def get_layaway_list(r: Response, order_by: Union[OrderByEnum, None] = None,
                           authorization: Union[str, None] = Header(dfault=None)):
    user, authenticated = auth(authorization_header=authorization)
    response = list()
    if not authenticated:
        r.status_code = status.HTTP_401_UNAUTHORIZED
        return ErrorResponse(message="bearer auth invalid")
    try:
        comics = db.get_layaway_list(db_session=db_session, user_uuid=user.id, order_by=order_by)
        if comics:
            for comic in comics:
                response.append(ComicResponse(
                    id=comic["id"],
                    title=comic["title"],
                    image=comic["image"],
                    onsaleDate=comic["onsaleDate"],
                ))
    except Exception as e:
        logger.err(LOGGER_FILE_NAME, "get_layaway_list", f"error get layaway: {str(e)}")
    return response
