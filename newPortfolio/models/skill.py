from peewee import CharField
from models.base_model import BaseModel
class Skill(BaseModel):
    name = CharField(max_length=255)
