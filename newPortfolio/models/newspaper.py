from peewee import CharField
from peewee import TextField
from peewee import ForeignKeyField
from models.base_model import BaseModel
from topic import Topic

class Newspaper(BaseModel):
    title = CharField(max_length=255)
    url = TextField()
    topic = ForeignKeyField(Topic, field = 'name', backref = 'newspapers', on_delete ='SET NULL ')
    