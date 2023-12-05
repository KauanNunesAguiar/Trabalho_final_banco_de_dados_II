from banco_de_dados.conexao import *

class Pagamento(Base):
    __tablename__ = 'Pagamento'
    ID_Pagamento = Column(Integer, primary_key=True)
    ID_Paciente = Column(Integer, ForeignKey('Paciente.ID_Paciente'), nullable=False)
    Valor = Column(DECIMAL(10,2), nullable=False)
    Data_Pagamento = Column(Date, nullable=False)
    Metodo_Pagamento = Column(String(50), nullable=False)
    Paciente = relationship('Paciente', back_populates='pagamentos')

def criar_pagamento(session, id_paciente, valor, data_pagamento, metodo_pagamento):
    pagamento = Pagamento(ID_Paciente=id_paciente, Valor=valor, Data_Pagamento=data_pagamento, Metodo_Pagamento=metodo_pagamento)
    session.add(pagamento)
    session.commit()
    return pagamento