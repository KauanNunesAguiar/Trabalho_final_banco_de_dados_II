from banco_de_dados.conexao import *

# =========[TABELA Usuario]=========
# CREATE TABLE Usuario (
#  ID_Usuario INT PRIMARY KEY IDENTITY(1,1),
#  Nome VARCHAR(50) NOT NULL,
#  Username VARCHAR(50) NOT NULL,
#  Senha VARCHAR(50) NOT NULL,
#  Nivel_Acesso CHAR(1) NOT NULL CONSTRAINT chk_nvl CHECK (Nivel_Acesso IN ('V', 'B', 'A'))
# );

class Usuario(Base):
    __tablename__ = 'Usuario'
    ID_Usuario = Column(Integer, primary_key=True)
    Nome = Column(String(NOME_MAX_LENGTH), nullable=False)
    Username = Column(String(USERNAME_MAX_LENGTH), nullable=False)
    Senha = Column(String(SENHA_MAX_LENGTH), nullable=False)
    Nivel_Acesso = Column(String(1), nullable=False)
    
def criar_usuario(session, nome, username, senha, nivel_acesso):
    usuario = Usuario(Nome=nome, Username=username, Senha=senha, Nivel_Acesso=nivel_acesso)
    session.add(usuario)
    session.commit()
    return usuario