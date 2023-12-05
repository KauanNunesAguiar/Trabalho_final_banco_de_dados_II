from banco_de_dados.conexao import *

class Agendamento(Base):
    __tablename__ = 'Agendamento'
    ID_Agendamento = Column(Integer, primary_key=True)
    ID_Paciente = Column(Integer, ForeignKey('Paciente.ID_Paciente'), nullable=False)
    ID_Fisioterapeuta = Column(Integer, ForeignKey('Fisioterapeuta.ID_Fisioterapeuta'), nullable=False)
    Data_Hora = Column(DateTime, nullable=False)
    Duracao = Column(Integer, nullable=False)
    Observacoes = Column(Text)
    Paciente = relationship('Paciente', back_populates='agendamentos')
    Fisioterapeuta = relationship('Fisioterapeuta', back_populates='agendamentos')
    
def criar_agendamento(session, id_paciente, id_fisioterapeuta, data_hora, duracao, observacoes):
    agendamento = Agendamento(ID_Paciente=id_paciente, ID_Fisioterapeuta=id_fisioterapeuta, Data_Hora=data_hora, Duracao=duracao, Observacoes=observacoes)
    session.add(agendamento)
    session.commit()
    return agendamento