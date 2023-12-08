from banco_de_dados.conexao import *

# =========[TABELA HistoricoMedico]=========
# CREATE TABLE HistoricoMedico (
#  ID_HistoricoMedico INT PRIMARY KEY IDENTITY(1,1),
#  ID_Paciente INT NOT NULL,
#  DataConsulta DATE NOT NULL,
#  Diagnostico TEXT NOT NULL,
#  TratamentoAnterior TEXT,
#  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente)
# );

class HistoricoMedico(Base):
    __tablename__ = 'HistoricoMedico'
    ID_HistoricoMedico = Column(Integer, primary_key=True)
    ID_Paciente = Column(Integer, ForeignKey('Paciente.ID_Paciente', ondelete='CASCADE'), nullable=False)
    DataConsulta = Column(Date, nullable=False)
    Diagnostico = Column(Text, nullable=False)
    TratamentoAnterior = Column(Text)
    
    Paciente = relationship("Paciente")
    
def criar_historico_medico(session, id_paciente, data_consulta, diagnostico, tratamento_anterior):
    historico_medico = HistoricoMedico(ID_Paciente=id_paciente, DataConsulta=data_consulta, Diagnostico=diagnostico, TratamentoAnterior=tratamento_anterior)
    session.add(historico_medico)
    session.commit()
    return historico_medico