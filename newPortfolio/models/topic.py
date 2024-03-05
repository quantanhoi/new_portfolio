from peewee import CharField
from models.base_model import BaseModel

class Topic(BaseModel):
    name = CharField(max_length=255)
    
    class Meta:
        table_name = 'topics'