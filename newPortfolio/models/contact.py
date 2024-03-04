from peewee import CharField
from models.base_model import BaseModel

class Contact(BaseModel):
    name = CharField(max_length=255)
    detail = CharField(max_length=255)
    