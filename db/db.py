from peewee import *

db = SqliteDatabase('usuarios.db')

class BaseModel(Model):
    class Meta:
        database = db

class (BaseModel):
    name = CharField(max_length=70)
    completed = bool ()
