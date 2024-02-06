from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from dotenv import load_dotenv
import os

# Inicialize o carregamento de variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__, template_folder='../templates')

swagger = Swagger(app)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:!Ak34ncs.m@ec2-54-232-63-26.sa-east-1.compute.amazonaws.com/db_123_ajuda'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Importação tardia para evitar importação cíclica
def register_blueprints():
    from app.routes import bp
    app.register_blueprint(bp, url_prefix='/api')

register_blueprints()
