from banco_de_dados.conexao import *

# =========[TABELA Relatorio]=========
# CREATE TABLE Relatorio (
#  ID_Relatorio INT PRIMARY KEY IDENTITY(1,1),
#  ID_Paciente INT NOT NULL,
#  Conteudo TEXT NOT NULL,
#  Data_Criacao DATE NOT NULL,
#  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente)
# );

class Relatorio(Base):
    __tablename__ = 'Relatorio'
    ID_Relatorio = Column(Integer, primary_key=True)
    ID_Paciente = Column(Integer, ForeignKey('Paciente.ID_Paciente', ondelete='CASCADE'), nullable=False)
    Conteudo = Column(Text, nullable=False)
    Data_Criacao = Column(Date, nullable=False)
    
    Paciente = relationship("Paciente")
    
def criar_relatorio(session, id_paciente, conteudo, data_criacao):
    relatorio = Relatorio(ID_Paciente=id_paciente, Conteudo=conteudo, Data_Criacao=data_criacao)
    session.add(relatorio)
    session.commit()
    return relatorio