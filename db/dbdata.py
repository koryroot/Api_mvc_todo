from peewee import *

db = SqliteDatabase('usuarios.db')

class BaseModel(Model):
    class Meta:
        database = db

class Todo (BaseModel):
    names = CharField(max_length=70)
    full = bool ()

def delete_cosa(id):
    try:
        return Todo.get(Todo.id == id).delete_instance()
    except Todo.DoesNotExist:
        return None

db.connect()
db.create_tables([Todo])