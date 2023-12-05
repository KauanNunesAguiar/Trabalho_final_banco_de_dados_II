from banco_de_dados.conexao import *

class Tratamento(Base):
    __tablename__ = 'Tratamento'
    ID_Tratamento = Column(Integer, primary_key=True)
    ID_Paciente = Column(Integer, ForeignKey('Paciente.ID_Paciente'), nullable=False)
    ID_Fisioterapeuta = Column(Integer, ForeignKey('Fisioterapeuta.ID_Fisioterapeuta'), nullable=False)
    Data_Inicio = Column(Date, nullable=False)
    Data_Fim = Column(Date, nullable=False)
    Diagnostico = Column(Text, nullable=False)
    Procedimentos = Column(Text)
    Paciente = relationship('Paciente', back_populates='tratamentos')
    Fisioterapeuta = relationship('Fisioterapeuta', back_populates='tratamentos')
    
def criar_tratamento(session, id_paciente, id_fisioterapeuta, data_inicio, data_fim, diagnostico, procedimentos):
    tratamento = Tratamento(ID_Paciente=id_paciente, ID_Fisioterapeuta=id_fisioterapeuta, Data_Inicio=data_inicio, Data_Fim=data_fim, Diagnostico=diagnostico, Procedimentos=procedimentos)
    session.add(tratamento)
    session.commit()
    return tratamento
