# Wendry Koralis

from fastapi import FastAPI
#from routers import usuario, secrets

app = FastAPI()

#app.include_router(usuario.router, tags=['Usuario'])
#app.include_router(secrets.router, tags=['Secrets'])

@app.get('/', tags=['Inicio'])
def read_root():
    return {
        'proyecto': 'Api de mvc todo',
        'docs': app.docs_url
}