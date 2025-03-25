from service.ResquestService import RequestService

class RequestController:
    def __init__(self) -> None:
        #Injetando a dependencia do service de request
        self.request_service = RequestService()
    @staticmethod
    def __treat_process(process: str) -> str:
        import re
        # Remove tudo que não for letra (a-z ou A-Z) e converte para minúsculo
        treated_process = re.sub(r'[^a-zA-Z]', '', process).lower()
        print('String tratada: {}'.format(treated_process))
        if not treated_process:
            raise ValueError("Dado inválido: a string tratada ficou vazia.")
        return treated_process
        
    async def handle_service_request(self,process:str) -> dict:
        if not isinstance(process, str):
            raise TypeError("O tipo do dado enviado foi incorreto")
        #Trata a string do processo passado na url
        treat_process = self.__treat_process(process=process)
        #Coleta os dados e armazena na variavel
        data = await self.request_service.get_sorted_data(treat_process)
        if data is None:
            return{'error': 'Esse notebook não foi encontrado!!'}
        return {'data': data}