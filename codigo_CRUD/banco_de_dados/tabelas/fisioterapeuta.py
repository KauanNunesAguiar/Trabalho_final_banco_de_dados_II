from banco_de_dados.conexao import *

class Fisioterapeuta(Base):
    __tablename__ = 'Fisioterapeuta'
    ID_Fisioterapeuta = Column(Integer, primary_key=True)
    Nome = Column(String(50), nullable=False)
    Especialidade = Column(String(50), nullable=False)
    Telefone = Column(String(15))
    Email = Column(String(50), nullable=False)
    
def criar_fisioterapeuta(session, nome, especialidade, telefone, email):
    fisioterapeuta = Fisioterapeuta(Nome=nome, Especialidade=especialidade, Telefone=telefone, Email=email)
    session.add(fisioterapeuta)
    session.commit()
    return fisioterapeuta