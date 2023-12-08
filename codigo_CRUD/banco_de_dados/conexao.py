from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, Time, Text, Float, ForeignKey, DECIMAL
from sqlalchemy.engine import URL
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship, Session, declarative_base
from datetime import datetime

CONTEUDO_MAX_LENGTH = 1000
DESCRICAO_MAX_LENGTH = 1000
DIAGNOSTICO_MAX_LENGTH = 1000
EMAIL_MAX_LENGTH = 50
ENDERECO_MAX_LENGTH = 50
ESPECIALIDADE_MAX_LENGTH = 50
NOME_MAX_LENGTH = 50
OBSERVACOES_MAX_LENGTH = 1000
PROCEDIMENTO_MAX_LENGTH = 1000
SENHA_MAX_LENGTH = 50
TELEFONE_MAX_LENGTH = 11
TRATAMENTO_ANTERIOR_MAX_LENGTH = 1000
USERNAME_MAX_LENGTH = 50

Base = declarative_base()

# Configuracoes do banco de dados
server = 'KAFEI-MATOIS-PR'
database = 'BD II'
driver = 'ODBC Driver 17 for SQL Server'

# Criar a URL de conexao do SQLAlchemy
db_url = URL.create(
    drivername='mssql+pyodbc',
    username='',
    password='',
    host=server,
    database=database,
    query={'driver': driver}
)

# Criar o mecanismo do SQLAlchemy
engine = create_engine(db_url)

# Criar uma sessão se não existir
session = Session(engine)