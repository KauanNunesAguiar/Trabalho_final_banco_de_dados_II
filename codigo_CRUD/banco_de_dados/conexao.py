from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, Text, ForeignKey, DECIMAL
from sqlalchemy.engine import URL
from sqlalchemy.orm import relationship, Session, declarative_base
from datetime import datetime

Base = declarative_base()

# Configuracoes do banco de dados
server = 'KAFEI-MATOIS-PR'
database = 'test'
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

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criar uma sessao para interagir com o banco de dados
session = Session(engine)