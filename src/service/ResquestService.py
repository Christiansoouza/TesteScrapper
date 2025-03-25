import requests
from retrying import retry
from bs4 import BeautifulSoup, Tag
from interfaces.interfaces import DataString

class RequestService:
    def __init__(self) -> None:
        #Os atributos são privados da classe
        self.__data = []
        self.__BASE_URL = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops' 

    @retry(stop_max_attempt_number=3)
    def __handle_request(self,url:str) -> str:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Não foi possível se conectar ao site")
        return response.text
    

    @staticmethod
    def __handle_parse_price(price_str: str) -> float:
        import re 
        """
        Remove caracteres não numéricos do preço e converte para float.
        Exemplo: '$700.00' -> 700.00
        """
        try:
            # Remove qualquer caractere que não seja dígito ou ponto
            price_cleaned = re.sub(r'[^\d.]', '', price_str)
            return float(price_cleaned)
        except ValueError:
            return float('inf')
    
    def get_data(self,process:str) -> list[dict]:
        """
        Obtem todos os dados e agrupa eles
        """
        print('esse é o processo {}'.format(process))
        for i in range(1,20):

            base = self.__BASE_URL + str(f'?page={i}')

            try:
                response = self.__handle_request(base)
                soup = BeautifulSoup(response, 'html.parser')

                # Encontra os títulos dos artigos (exemplo: dentro de <h2>)
                captions = soup.find_all('div',class_="caption")

                # Exibe os títulos extraídos
                for caption in captions:
                    if isinstance(caption, Tag):
                        price_tag = caption.find('h4', class_='price float-end card-title pull-right')
                        title_tag = caption.find('a', class_='title')
                        description_tag = caption.find('p', class_='description card-text')

                    # Verifica se o título existe e se contém o texto procurado (case insensitive)
                    
                    if title_tag and process in title_tag.get_text(strip=True).lower():
                        price_text = price_tag.get_text(strip=True) if price_tag else ""
                        notebook_title = title_tag.get_text(strip=True)
                        notebook_description = description_tag.get_text(strip=True) if description_tag else ""

                        self.__data.append({
                            'page': i,
                            'notebook': notebook_title,
                            'price': price_text,
                            'price_value': self.__handle_parse_price(price_text),
                            'description': notebook_description
                        })
            except Exception as e:
                print(e)
        return self.__data
    async def get_sorted_data(self,process:str):
        """
        Retorna os dados coletados ordenados do menor para o maior preço.
        """
        # Se os dados ainda não foram carregados, faz a coleta
        if not self.__data:
            self.get_data(process=process)
        return sorted(self.__data, key=lambda x: x.get('price_value', float('inf')))