from banco_de_dados.conexao import *

# =========[TABELA Agendamento]=========
# CREATE TABLE Agendamento (
#  ID_Agendamento INT PRIMARY KEY IDENTITY(1,1),
#  ID_Paciente INT NOT NULL,
#  ID_Fisioterapeuta INT NOT NULL,
#  Data_Hora DATETIME NOT NULL,
#  Duracao TIME NOT NULL,
#  Observacoes TEXT,
#  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente),
#  FOREIGN KEY (ID_Fisioterapeuta) REFERENCES Fisioterapeuta(ID_Fisioterapeuta)
# );

class Agendamento(Base):
    __tablename__ = 'Agendamento'
    ID_Agendamento = Column(Integer, primary_key=True)
    ID_Paciente = Column(Integer, ForeignKey('Paciente.ID_Paciente', ondelete='CASCADE'), nullable=False)
    ID_Fisioterapeuta = Column(Integer, ForeignKey('Fisioterapeuta.ID_Fisioterapeuta', ondelete='CASCADE'), nullable=False)
    Data_Hora = Column(DateTime, nullable=False)
    Duracao = Column(String, nullable=False)  # Alteração do tipo de dados para String
    Observacoes = Column(Text)
    
    paciente = relationship("Paciente")
    fisioterapeuta = relationship("Fisioterapeuta")

def criar_agendamento(session, id_paciente, id_fisioterapeuta, data_hora, duracao, observacoes):
    agendamento = Agendamento(ID_Paciente=id_paciente, ID_Fisioterapeuta=id_fisioterapeuta, Data_Hora=data_hora, Duracao=duracao, Observacoes=observacoes)
    session.add(agendamento)
    session.commit()
    
    return agendamento
    