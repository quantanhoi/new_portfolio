from peewee import Model
from database.database import db 


class BaseModel(Model):
    """A base model that will use our PostgreSQL database."""
    class Meta:
        database = db
        #schema = 'db2sttrthie'  #set schema to db2sttrthie
