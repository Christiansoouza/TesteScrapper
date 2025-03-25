FROM python:3.9-slim

# Define o diretório de trabalho como /src
WORKDIR /src

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia TODO o conteúdo para /src no container
COPY . .

# Configura o Python para encontrar os módulos (agora em /src)
ENV PYTHONPATH="${PYTHONPATH}:/src"

# Porta que o FastAPI vai usar
EXPOSE 8080

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]