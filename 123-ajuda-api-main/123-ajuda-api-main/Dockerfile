FROM python:3.8-slim

WORKDIR /app

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip3 install -r requirements.txt

# Copie o restante do código para o contêiner
COPY . .


