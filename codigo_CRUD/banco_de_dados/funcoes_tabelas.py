from banco_de_dados.tabelas.agendamento import *
from banco_de_dados.tabelas.fisioterapeuta import *
from banco_de_dados.tabelas.historico_medico import *
from banco_de_dados.tabelas.pagamento import *
from banco_de_dados.tabelas.paciente import *
from banco_de_dados.tabelas.relatorio import *
from banco_de_dados.tabelas.tratamento import *
from banco_de_dados.tabelas.usuario import *

DESCRICAO_MAX_LENGTH = 1000
DIAGNOSTICO_MAX_LENGTH = 1000
EMAIL_MAX_LENGTH = 50
ENDERECO_MAX_LENGTH = 50
ESPECIALIDADE_MAX_LENGTH = 50
NOME_MAX_LENGTH = 50
OBSERVACOES_MAX_LENGTH = 1000
PROCEDIMENTO_MAX_LENGTH = 1000
SENHA_MAX_LENGTH = 50
TELEFONE_MAX_LENGTH = 11
TRATAMENTO_ANTERIOR_MAX_LENGTH = 1000
USERNAME_MAX_LENGTH = 50

# Relacionamentos bidirecionais
Paciente.agendamentos = relationship('Agendamento', back_populates='Paciente')
Paciente.historico_medico = relationship('HistoricoMedico', back_populates='Paciente')
Paciente.tratamentos = relationship('Tratamento', back_populates='Paciente')
Paciente.pagamentos = relationship('Pagamento', back_populates='Paciente')
Paciente.relatorios = relationship('Relatorio', back_populates='Paciente')

Fisioterapeuta.agendamentos = relationship('Agendamento', back_populates='Fisioterapeuta')
Fisioterapeuta.tratamentos = relationship('Tratamento', back_populates='Fisioterapeuta')