from banco_de_dados.funcoes_tabelas import *

# Definir funcoes para melhorar a interacao com o usuario
def menu(opcoes):
    while True:
        print("\nEscolha uma das opcoes abaixo:")
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i} - {opcao}")

        print(f"{len(opcoes) + 1} - Voltar")
        escolha = input("Digite sua opcao: ")

        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(opcoes) + 1:
                return escolha
            else:
                print("Opcao invalida. Tente novamente.")
        except ValueError:
            print("Digite um numero valido.")
            
def id_existe(id, tabela):
    if tabela == 'Paciente':
        return session.query(Paciente).filter(Paciente.ID_Paciente == id).first()
    elif tabela == 'Fisioterapeuta':
        return session.query(Fisioterapeuta).filter(Fisioterapeuta.ID_Fisioterapeuta == id).first()
    elif tabela == 'Usuario':
        return session.query(Usuario).filter(Usuario.ID_Usuario == id).first()
    elif tabela == 'Agendamento':
        return session.query(Agendamento).filter(Agendamento.ID_Agendamento == id).first()
    elif tabela == 'HistoricoMedico':
        return session.query(HistoricoMedico).filter(HistoricoMedico.ID_HistoricoMedico == id).first()
    elif tabela == 'Tratamento':
        return session.query(Tratamento).filter(Tratamento.ID_Tratamento == id).first()
    elif tabela == 'Pagamento':
        return session.query(Pagamento).filter(Pagamento.ID_Pagamento == id).first()
    elif tabela == 'Relatorio':
        return session.query(Relatorio).filter(Relatorio.ID_Relatorio == id).first()
    else:
        return None

            