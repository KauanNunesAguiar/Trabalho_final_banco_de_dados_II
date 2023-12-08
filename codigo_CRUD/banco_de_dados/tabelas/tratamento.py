from banco_de_dados.conexao import *

# =========[TABELA Tratamento]=========
# CREATE TABLE Tratamento (
#  ID_Tratamento INT PRIMARY KEY IDENTITY(1,1),
#  ID_Paciente INT NOT NULL,
#  ID_Fisioterapeuta INT NOT NULL,
#  Data_Inicio DATE NOT NULL,
#  Data_Fim DATE NOT NULL,
#  Diagnostico TEXT NOT NULL,
#  Procedimentos TEXT,
#  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente),
#  FOREIGN KEY (ID_Fisioterapeuta) REFERENCES Fisioterapeuta(ID_Fisioterapeuta)
# );

class Tratamento(Base):
    __tablename__ = 'Tratamento'
    ID_Tratamento = Column(Integer, primary_key=True)
    ID_Paciente = Column(Integer, ForeignKey('Paciente.ID_Paciente', ondelete='CASCADE'), nullable=False)
    ID_Fisioterapeuta = Column(Integer, ForeignKey('Fisioterapeuta.ID_Fisioterapeuta', ondelete='CASCADE'), nullable=False)
    Data_Inicio = Column(Date, nullable=False)
    Data_Fim = Column(Date, nullable=False)
    Diagnostico = Column(Text, nullable=False)
    Procedimentos = Column(Text)
    
    Paciente = relationship("Paciente")
    Fisioterapeuta = relationship("Fisioterapeuta")
    
def criar_tratamento(session, id_paciente, id_fisioterapeuta, data_inicio, data_fim, diagnostico, procedimentos):
    tratamento = Tratamento(ID_Paciente=id_paciente, ID_Fisioterapeuta=id_fisioterapeuta, Data_Inicio=data_inicio, Data_Fim=data_fim, Diagnostico=diagnostico, Procedimentos=procedimentos)
    session.add(tratamento)
    session.commit()
    return tratamento
