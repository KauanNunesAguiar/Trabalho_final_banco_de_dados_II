from banco_de_dados.conexao import *

# =========[TABELA fisioterapeuta]=========
# CREATE TABLE Fisioterapeuta (
#  ID_Fisioterapeuta INT PRIMARY KEY IDENTITY(1,1),
#  Nome VARCHAR(50) NOT NULL,
#  Especialidade VARCHAR(50) NOT NULL,
#  Telefone VARCHAR(13),
#  Email VARCHAR(50) NOT NULL
# );

class Fisioterapeuta(Base):
    __tablename__ = 'Fisioterapeuta'
    ID_Fisioterapeuta = Column(Integer, primary_key=True)
    Nome = Column(String(NOME_MAX_LENGTH), nullable=False)
    Especialidade = Column(String(ESPECIALIDADE_MAX_LENGTH), nullable=False)
    Telefone = Column(String(TELEFONE_MAX_LENGTH))
    Email = Column(String(EMAIL_MAX_LENGTH), nullable=False)
    
def criar_fisioterapeuta(session, nome, especialidade, telefone, email):
    fisioterapeuta = Fisioterapeuta(Nome=nome, Especialidade=especialidade, Telefone=telefone, Email=email)
    session.add(fisioterapeuta)
    session.commit()
    return fisioterapeuta