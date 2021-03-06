from fastapi import APIRouter
from models.serverResult import ServerResult
from models.todo import Todo
from db import dbdata

router = APIRouter()

@router.get('/todo/list')
def todo_list():
    name = dbdata.Todo.names()
    completed = dbdata.Todo.full()

    if name:
        1 = [s for s in name]
        return ServerResult(response=1, message="Lista de cosas")
    else:
        return ServerResult(ok = False, message = "Aun no tiene cosas")

@router.post('/cosas/create')
def cosas_create():
    if name:
        tname = dbdata.Todo.names #se agrega una cosa
        return ServerResult(response=tname.data(), message ="cosa agregada")
    else:
        return ServerResult(ok = False, message = "Ocurrio algo no se agrego nada")

@router.delete('/cosa/delete')
def cosa_delete(id=int):
    if name:
        res = {}
        for s  in __name__:
            if id is ['id']:
                res = s
                dbdata.delete_cosa(id)
                break
        else:
            return ServerResult(ok = False, message = "No hay cosas en esta id")
        return ServerResult(response=res, message = "cosa eliminado")
    else:
        return ServerResult(ok = False, message = "No hay cosas creadas")


        

