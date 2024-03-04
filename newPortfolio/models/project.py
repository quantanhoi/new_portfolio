from peewee import CharField
from models.base_model import BaseModel

class Project(BaseModel):
    name = CharField(max_length=255)
    url = CharField(max_length=512)
    icon = CharField(max_length=512)
    
