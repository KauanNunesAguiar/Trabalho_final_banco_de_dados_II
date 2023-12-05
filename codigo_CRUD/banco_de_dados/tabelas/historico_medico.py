from banco_de_dados.conexao import *

class HistoricoMedico(Base):
    __tablename__ = 'HistoricoMedico'
    ID_HistoricoMedico = Column(Integer, primary_key=True)
    ID_Paciente = Column(Integer, ForeignKey('Paciente.ID_Paciente'), nullable=False)
    DataConsulta = Column(Date, nullable=False)
    Diagnostico = Column(Text, nullable=False)
    TratamentoAnterior = Column(Text)
    Paciente = relationship('Paciente', back_populates='historico_medico')
    
def criar_historico_medico(session, id_paciente, data_consulta, diagnostico, tratamento_anterior):
    historico_medico = HistoricoMedico(ID_Paciente=id_paciente, DataConsulta=data_consulta, Diagnostico=diagnostico, TratamentoAnterior=tratamento_anterior)
    session.add(historico_medico)
    session.commit()
    return historico_medico