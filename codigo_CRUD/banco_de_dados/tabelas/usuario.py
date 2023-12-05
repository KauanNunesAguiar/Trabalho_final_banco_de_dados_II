from banco_de_dados.conexao import *

class Usuario(Base):
    __tablename__ = 'Usuario'
    ID_Usuario = Column(Integer, primary_key=True)
    Nome = Column(String(50), nullable=False)
    Username = Column(String(50), nullable=False)
    Senha = Column(String(50), nullable=False)

def criar_usuario(session, nome, username, senha):
    usuario = Usuario(Nome=nome, Username=username, Senha=senha)
    session.add(usuario)
    session.commit()
    return usuario