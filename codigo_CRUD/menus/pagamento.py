from menus.inicial import *

opcoes_menu_pagamentos = [
    "Criar novo pagamento",
    "Editar pagamento",
    "Excluir pagamento",
    "Listar pagamentos"
]

def menu_pagamentos():
    opcao = menu(opcoes_menu_pagamentos)
    match opcao:
        case 1:
            menu_criar_pagamento()
        case 2:
            menu_editar_pagamento()
        case 3:
            menu_excluir_pagamento()
        case 4:
            menu_listar_pagamentos()
        case 5:
            menu_inicial()
        case _:
            print("Opcao invalida. Tente novamente.")
            menu_pagamentos()
    
def menu_criar_pagamento():
    print("\nCriar novo pagamento")
    id_paciente = input("Digite o ID do paciente: ")
    id_tratamento = input("Digite o ID do tratamento: ")
    valor = input("Digite o valor do pagamento: ")
    data_pagamento = input("Digite a data do pagamento (AAAA-MM-DD): ")
    
    if verificar_dados_pagamento(session, id_paciente, id_tratamento, valor, data_pagamento):
        pagamento = criar_pagamento(session, id_paciente, id_tratamento, valor, data_pagamento)
        print(f"Pagamento criado com sucesso. ID: {pagamento.ID_Pagamento}")
    else:
        print("Erro ao criar pagamento.")
        
    menu_pagamentos()
    
def menu_editar_pagamento():
    print("\nEditar pagamento")
    id_pagamento = input("Digite o ID do pagamento: ")
    if not id_existe(id_pagamento, 'Pagamento'):
        print("Pagamento nao encontrado.")
    else:
        id_paciente = input("Digite o ID do paciente: ")
        id_tratamento = input("Digite o ID do tratamento: ")
        valor = input("Digite o valor do pagamento: ")
        data_pagamento = input("Digite a data do pagamento (AAAA-MM-DD): ")
    
        if verificar_dados_pagamento(session, id_paciente, id_tratamento, valor, data_pagamento):
            pagamento = session.query(Pagamento).filter(Pagamento.ID_Pagamento == id_pagamento).first()
            pagamento.ID_Paciente = id_paciente
            pagamento.ID_Tratamento = id_tratamento
            pagamento.Valor = valor
            pagamento.Data_Pagamento = data_pagamento
            session.commit()
            print(f"Pagamento editado com sucesso. ID: {pagamento.ID_Pagamento}")
        else:
            print("Erro ao editar pagamento.")
        
    menu_pagamentos()
    
def menu_excluir_pagamento():
    print("\nExcluir pagamento")
    id_pagamento = input("Digite o ID do pagamento: ")
    if not(id_existe(id_pagamento, 'Pagamento')):
        print("Pagamento nao encontrado.")
    else:
        pagamento = session.query(Pagamento).filter(Pagamento.ID_Pagamento == id_pagamento).first()
        session.delete(pagamento)
        session.commit()
        print(f"Pagamento excluido com sucesso. ID: {id_pagamento}")
    menu_pagamentos()

def menu_listar_pagamentos():
    print("\nListar pagamentos")
    pagamentos = session.query(Pagamento).all()
    for pagamento in pagamentos:
        print(f"ID: {pagamento.ID_Pagamento} | ID Paciente: {pagamento.ID_Paciente} | ID Tratamento: {pagamento.ID_Tratamento} | Valor: {pagamento.Valor} | Data do Pagamento: {pagamento.Data_Pagamento}")
    menu_pagamentos()
    
def verificar_dados_pagamento(session, id_paciente, id_tratamento, valor, data_pagamento):
    try:
        assert isinstance(id_paciente, int) and id_existe(id_paciente, 'Paciente')
        assert isinstance(id_tratamento, int) and id_existe(id_tratamento, 'Tratamento')
        assert isinstance(valor, float) and valor >= 0
        data_pagamento = datetime.strptime(data_pagamento, "%Y-%m-%d").date()
        
        return True

    except (ValueError, AssertionError) as e:
        session.rollback()
        return None