from banco_de_dados.conexao import *

class Paciente(Base):
    __tablename__ = 'Paciente'
    ID_Paciente = Column(Integer, primary_key=True)
    Nome = Column(String(50), nullable=False)
    Data_Nascimento = Column(Date, nullable=False)
    Endereco = Column(String(50), nullable=False)
    Telefone = Column(String(15))
    Email = Column(String(50), nullable=False)
    
def criar_paciente(session, nome, data_nascimento, endereco, telefone, email):
        paciente = Paciente(Nome=nome, Data_Nascimento=data_nascimento, Endereco=endereco, Telefone=telefone, Email=email)
        session.add(paciente)
        session.commit()
        return paciente
