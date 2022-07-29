from email.message import Message
from importlib.resources import contents
from unicodedata import name
from django.dispatch import receiver
from pydantic import BaseModel
from enum import Enum
from itertools import product
from typing import Union
from fastapi import FastAPI
from h11 import PRODUCT_ID
import idna
server = FastAPI()

# @server.get("/")
# def hello():
#     return {"name": "kaoutar", "age": 21, "profession": "computer science"}
    
# @server.get("/message")
# def hello():
#     return  ["how is it going?",'good']

# @server.get("/search/repositories")
# def hello():
#     return {"msg": "true"}

# @server.get("/drink")
# def get_drink():
#     return {"msg": "juice"}
    

# products_kaoutar = ["t-shirt", "shoes", "hat",'jacket']  
# products_hassane = ['sunglasses','pants','watch']  

# @server.get("/users")
# def etini_kolchi():
#     return []

# @server.get("/products")
# def etini_kolchi():
#     return products_kaoutar

# @server.get("/product/{product_id}")
# def get_product(product_id: int, username:str = 'kaoutar'):
#     if username == "kaoutar":
#         return products_kaoutar[product_id]
#     if username == "hassane":
#         return products_hassane[product_id]



# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lanet = "lenet"


# @server.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}

    
    
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None

# @server.post("/items")   
# def create_item(item: Item):
#     print(item)
#     return 'received'

# @server.get("/cafe")    
# def cafe_name():
#     return 'miligusto'

# cafe_names = ['oregal', 'bleucafe', 'beli', 'ayden']
# @server.get("/cafe/")    
# def get_coffee(cafes_id: int):
#     return cafe_names[cafes_id]



# @server.get("/cafes")    
# def cafes_name():
#     return cafe_names




# # name is query parameter
# @server.get("/hi")          # <----- makaynch hna
# def get_say(name):          # <----- kayn hna
#     return 'hi ' + name 

# # name is path parameter
# @server.get("/hi/{name}")   # <----- kayn hna
# def get_say(name):          # <----- kayn hna
#     return 'hi ' + name 


# class SMS(BaseModel):
#     sender: str
#     receiver: str
#     contents: str
#     time: str
    
# @server.post("/message")
# def send_message(sms: SMS):
#     print(sms)
#     return 'the message has been sent'





# @server.get("/person")
# def my_person(name):
#     for x in list:
#         if x['name']==name:
#             return x["salary"]



# class Person (BaseModel):
#     name: str
#     job: str
#     age: int
#     salary: int
                
# @server.post("/person")
# def my_person(p:Person):
#     list.append(p)       
#     print(list)
#     return "completed"
list = [
    {"name" : "elyana", "age": 22, "job" : "computer_science", "salary" : 300000 },
    {"name" : "dima", "age" : 23, "job" : "enginner", "salary" : 40000},
    {"name": "diana", "age" : 25, "job":"entreprenneur", "salary": 540000}]

@server.get("/person")    
def my_person(age:int):
    new_list=[]
    for x in list :
        if x["age"] >=age:
            new_list.append(x)
    return new_list
        


