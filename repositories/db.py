from typing import Union, Dict, List

import pymongo
from pymongo.collection import Collection

import logger
from models.enums import OrderByEnum


def get_layaway_list(db_session: Collection, user_uuid: str,
                     order_by: Union[OrderByEnum, None] = None) -> List[Dict[str, any]]:
    try:
        user_exist = db_session.layaways.find({user_uuid: {"$exists": True}})
        user = list(user_exist)
        if user:
            comics = db_session.layaways.find({"_id": user[0].get("_id")})
            comics = list(comics)
            if comics:
                comics = comics[0].get(user_uuid)
                if order_by:
                    order = order_by.value
                    if order[0] == "-":
                        comics = sorted(comics, key=lambda c: c[order[1:]], reverse=True)
                    else:
                        comics = sorted(comics, key=lambda c: c[order], reverse=False)
                return comics
    except Exception as e:
        logger.err("repositories/db.py", "get_layaway_list", f"error on get layaway: {str(e)}")
        raise e
