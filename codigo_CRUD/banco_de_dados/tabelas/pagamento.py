from banco_de_dados.conexao import *

# =========[TABELA Pagamento]=========
# CREATE TABLE Pagamento (
#  ID_Pagamento INT PRIMARY KEY IDENTITY(1,1),
#  ID_Paciente INT NOT NULL,
#  Valor DECIMAL(10,2) NOT NULL,
#  Data_Pagamento DATE NOT NULL,
#  Metodo_Pagamento CHAR(1) NOT NULL CONSTRAINT chk_pag CHECK (Metodo_Pagamento IN  ('C', 'D', 'E', 'P')),
#  FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente)
# );

class Pagamento(Base):
    __tablename__ = 'Pagamento'
    ID_Pagamento = Column(Integer, primary_key=True)
    ID_Paciente = Column(Integer, ForeignKey('Paciente.ID_Paciente', ondelete='CASCADE'), nullable=False)
    Valor = Column(Float, nullable=False)
    Data_Pagamento = Column(Date, nullable=False)
    Metodo_Pagamento = Column(String(1), nullable=False)
    
    Paciente = relationship("Paciente")
    
def criar_pagamento(session, id_paciente, valor, data_pagamento, metodo_pagamento):
    pagamento = Pagamento(ID_Paciente=id_paciente, Valor=valor, Data_Pagamento=data_pagamento, Metodo_Pagamento=metodo_pagamento)
    session.add(pagamento)
    session.commit()
    return pagamento