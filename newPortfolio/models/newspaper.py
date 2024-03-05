from peewee import CharField
from peewee import TextField
from peewee import ForeignKeyField
from models.base_model import BaseModel
from models.topic import Topic

class Newspaper(BaseModel):
    title = CharField(max_length=255)
    url = TextField()
    topic = ForeignKeyField(Topic, field = 'name', backref = 'newspapers', on_delete ='SET NULL', column_name = 'topic')
    
    class Meta:
        table_name = 'newspapers'
        
    