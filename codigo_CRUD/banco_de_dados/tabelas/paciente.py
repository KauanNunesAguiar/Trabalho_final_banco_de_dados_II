from banco_de_dados.conexao import *

# =========[TABELA Paciente]=========
# CREATE TABLE Paciente (
#  ID_Paciente INT PRIMARY KEY IDENTITY(1,1),
#  Nome VARCHAR(50) NOT NULL,
#  Data_Nascimento DATE NOT NULL,
#  Endereco VARCHAR(50) NOT NULL,
#  Telefone VARCHAR(13),
#  Email VARCHAR(50) NOT NULL
# );

class Paciente(Base):
    __tablename__ = 'Paciente'
    ID_Paciente = Column(Integer, primary_key=True)
    Nome = Column(String(NOME_MAX_LENGTH), nullable=False)
    Data_Nascimento = Column(Date, nullable=False)
    Endereco = Column(String(ENDERECO_MAX_LENGTH), nullable=False)
    Telefone = Column(String(TELEFONE_MAX_LENGTH))
    Email = Column(String(EMAIL_MAX_LENGTH), nullable=False)
    
def criar_paciente(session, nome, data_nascimento, endereco, telefone, email):
    paciente = Paciente(Nome=nome, Data_Nascimento=data_nascimento, Endereco=endereco, Telefone=telefone, Email=email)
    session.add(paciente)
    session.commit()
    return paciente
