from peewee import *

db = SqliteDatabase('usuarios.db')

class BaseModel(Model):
    class Meta:
        database = db

class Todo (BaseModel):
    names = CharField(max_length=70)
    full = bool ()

db.connect()
db.create_tables([Todo])