from enum import Enum


class OrderByEnum(str, Enum):
    id_asc = 'id'
    id_des = '-id'
    title_asc = "title"
    title_des = "-title"
    onsale_date_asc = 'onsaleDate'
    onsale_date_des = '-onsaleDate'
