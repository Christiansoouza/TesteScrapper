from fastapi import FastAPI
from .Routes import route as testando

def load_routes(app:FastAPI):
    print('cheguei')
    app.include_router(testando, prefix='/api')