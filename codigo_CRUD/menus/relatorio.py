from menus.inicial import *

opcoes_menu_relatorios = [
    "Criar novo relatorio",
    "Editar relatorio",
    "Excluir relatorio",
    "Listar relatorios"
]

def menu_relatorios():
    opcao = menu(opcoes_menu_relatorios)
    match opcao:
        case 1:
            menu_criar_relatorio()
        case 2:
            menu_editar_relatorio()
        case 3:
            menu_excluir_relatorio()
        case 4:
            menu_listar_relatorios()
        case 5:
            menu_inicial()
        case _:
            print("Opcao invalida. Tente novamente.")
            menu_relatorios()
    
def menu_criar_relatorio():
    print("\nCriar novo relatorio")
    id_paciente = input("Digite o ID do paciente: ")
    id_tratamento = input("Digite o ID do tratamento: ")
    data = input("Digite a data (AAAA-MM-DD): ")
    descricao = input("Digite a descricao: ")
    
    if verificar_dados_relatorio(session, id_paciente, id_tratamento, data, descricao):
        relatorio = criar_relatorio(session, id_paciente, id_tratamento, data, descricao)
        print(f"Relatorio criado com sucesso. ID: {relatorio.ID_Relatorio}")
    else:
        print("Erro ao criar relatorio.")
        
    menu_relatorios()

def menu_editar_relatorio():
    print("\nEditar relatorio")
    id_relatorio = input("Digite o ID do relatorio: ")
    if not id_existe(id_relatorio, 'Relatorio'):
        print("Relatorio nao encontrado.")
    else:
        id_paciente = input("Digite o ID do paciente: ")
        id_tratamento = input("Digite o ID do tratamento: ")
        data = input("Digite a data (AAAA-MM-DD): ")
        descricao = input("Digite a descricao: ")
    
        if verificar_dados_relatorio(session, id_paciente, id_tratamento, data, descricao):
            relatorio = session.query(Relatorio).filter(Relatorio.ID_Relatorio == id_relatorio).first()
            relatorio.ID_Paciente = id_paciente
            relatorio.ID_Tratamento = id_tratamento
            relatorio.Data = data
            relatorio.Descricao = descricao
            session.commit()
            print(f"Relatorio editado com sucesso. ID: {relatorio.ID_Relatorio}")
        else:
            print("Erro ao editar relatorio.")
        
    menu_relatorios()
    
def menu_excluir_relatorio():
    print("\nExcluir relatorio")
    id_relatorio = input("Digite o ID do relatorio: ")
    if not(id_existe(id_relatorio, 'Relatorio')):
        print("Relatorio nao encontrado.")
    else:
        relatorio = session.query(Relatorio).filter(Relatorio.ID_Relatorio == id_relatorio).first()
        session.delete(relatorio)
        session.commit()
        print(f"Relatorio excluido com sucesso. ID: {id_relatorio}")
    menu_relatorios()
    
def menu_listar_relatorios():
    print("\nListar relatorios")
    relatorios = session.query(Relatorio).all()
    for relatorio in relatorios:
        print(f"ID: {relatorio.ID_Relatorio} | ID Paciente: {relatorio.ID_Paciente} | ID Tratamento: {relatorio.ID_Tratamento} | Data: {relatorio.Data} | Descricao: {relatorio.Descricao}")
    menu_relatorios()
    
def verificar_dados_relatorio(session, id_paciente, id_tratamento, data, descricao):
    try:
        assert isinstance(id_paciente, int) and id_existe(id_paciente, 'Paciente')
        assert isinstance(id_tratamento, int) and id_existe(id_tratamento, 'Tratamento')
        data = datetime.strptime(data, "%Y-%m-%d").date()
        assert isinstance(descricao, str) and len(descricao) <= DESCRICAO_MAX_LENGTH
        
        return True

    except (ValueError, AssertionError) as e:
        session.rollback()
        return None