# 123-ajuda-api TCC 
Este é uma API para trabalho de TCC 123 Ajuda das alunas Lais Alves e Anelise Costa com a orientação do Professor Fábio Henrique M Oliveira.

Esta API Flask fornece informações sobre unidades de saúde. Você pode usar esta API para obter detalhes sobre diferentes unidades de saúde, filtrar por abrangência, estado e horário integral.

## Pré-requisitos

- Python 3.x instalado em seu sistema. Você pode baixar o Python em [python.org](https://www.python.org/).
- pip, o gerenciador de pacotes do Python.

## Configuração do Ambiente Virtual

### Clone este repositório em seu sistema

```bash
git clone https://github.com/infocbra/123-ajuda-api.git
cd 123-ajuda-api
```

### Crie e ative um ambiente virtual para o projeto
```bash
python -m venv venv
source venv/bin/activate   # No Windows: venv\Scripts\activate
```

### Instale as dependências do projeto
```bash
pip install -r requirements.txt
```

### Após configurar o ambiente virtual e instalar as dependências, inicie o servidor Flask
```bash
flask run
```

## Documentação da API

A documentação da API, gerada pelo Swagger, está disponível em [http://localhost:5000/api/apidocs](http://localhost:5000/apidocs). Utilize o Swagger para explorar e testar as diferentes rotas da API.

### Parâmetros de Consulta

- **abrangencia**: Filtro por abrangência da unidade de saúde.
- **uf**: Filtro por estado da unidade de saúde.
- **isFullTime**: Filtro por horário integral da unidade de saúde.

## Exemplos de Requisições

- **Obter todas as unidades de saúde**:


  GET http://localhost:5000/api/unidades_de_saude

- **Filtrar por abrangência:**:


  GET http://localhost:5000/api/unidades_de_saude?abrangencia=Gama

- **Filtrar por estado e horário integral::**:

  GET http://localhost:5000/api/unidades_de_saude?uf=sao+paulo&isFullTime=true


## Rotas no Ambiente de Produção

- **Rota Principal da api**:

  GET https://123ajuda.tech/api

- **Filtrar por abrangência:**:

  GET https://123ajuda.tech/api/unidades_de_saude?abrangencia=Gama

- **Filtrar por estado e horário integral::**:

  GET https://123ajuda.tech/api/unidades_de_saude?uf=sao+paulo&isFullTime=true