from fastapi import APIRouter,Depends
from controller.RequestController import RequestController

route = APIRouter()

@route.post('/scrapper/{id}')
def requestRouter(id:str,request_controller: RequestController = Depends()):
    return request_controller.handle_service_request(process=id)