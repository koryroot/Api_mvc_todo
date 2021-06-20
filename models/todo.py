from pydantic import BaseModel

class Todo (BaseModel):
    name = ''
    completed = bool
 