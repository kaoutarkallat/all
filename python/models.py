from enum import Enum
from typing import Optional
import uuid
from pydantic import UUID4, BaseModel




from pydantic import BaseModel
from uuid import UUID, uuid4


class User(BaseModel):
    pass
class Gender(str, Enum):
    male = "male"
    female = "female"
class Role(str, Enum):
    admin = "admin"
    student= "student"


    id: Optional[UUID] = UUID4
    first_name: str
    last_name: str
    middle_name: str
    gender: Gender


from typing import Union
from pydantic import BaseModel


from fastapi import FastAPI

app = FastAPI()
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, size: Union[str, None] = None, color: Union[str,None]=None):
    return {"item_id": item_id, "size": size, "color": color}
    
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}