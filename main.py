# Wendry Koralis

from fastapi import FastAPI
from routers import todo

app = FastAPI()
app.include_router(todo.router, tags=['Cosa'])


@app.get('/', tags=['Inicio'])
def read_root():
    return {
        'proyecto': 'Api de mvc todo',
        'docs': app.docs_url
}