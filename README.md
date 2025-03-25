# API FastAPI - Web Scraper

Este projeto utiliza FastAPI para criar uma API de web scraping. Ele roda dentro de um contêiner Docker e pode ser facilmente executado seguindo os passos abaixo.

## 🎯 Objetivo
Essa aplicação tem o propósito de buscar todos os dados dos notebooks e ordená-los do menor para o maior preço.

## 🚀 Como rodar com Docker

### 1️⃣ **Construir e rodar o container**
Execute o seguinte comando para construir e iniciar o container em segundo plano:

#Construindo o container
```sh
docker compose up --build -d 

##Testar a aplicação
```sh
http://localhost:8000/docs