from banco_de_dados.conexao import *

class Relatorio(Base):
    __tablename__ = 'Relatorio'
    ID_Relatorio = Column(Integer, primary_key=True)
    ID_Paciente = Column(Integer, ForeignKey('Paciente.ID_Paciente'), nullable=False)
    Conteudo = Column(Text, nullable=False)
    Data_Criacao = Column(Date, nullable=False)
    Paciente = relationship('Paciente', back_populates='relatorios')
    
def criar_relatorio(session, id_paciente, conteudo, data_criacao):
    relatorio = Relatorio(ID_Paciente=id_paciente, Conteudo=conteudo, Data_Criacao=data_criacao)
    session.add(relatorio)
    session.commit()
    return relatorio