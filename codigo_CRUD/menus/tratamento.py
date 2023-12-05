from menus.inicial import *

opcoes_menu_tratamentos = [
    "Criar novo tratamento",
    "Editar tratamento",
    "Excluir tratamento",
    "Listar tratamentos"
]

def menu_tratamentos():
    opcao = menu(opcoes_menu_tratamentos)
    match opcao:
        case 1:
            menu_criar_tratamento()
        case 2:
            menu_editar_tratamento()
        case 3:
            menu_excluir_tratamento()
        case 4:
            menu_listar_tratamentos()
        case 5:
            menu_inicial()
        case _:
            print("Opcao invalida. Tente novamente.")
            menu_tratamentos()
            
def menu_criar_tratamento():
    print("\nCriar novo tratamento")
    id_paciente = input("Digite o ID do paciente: ")
    id_fisioterapeuta = input("Digite o ID do fisioterapeuta: ")
    data_inicio = input("Digite a data de inicio do tratamento (AAAA-MM-DD): ")
    data_fim = input("Digite a data de fim do tratamento (AAAA-MM-DD): ")
    diagnostico = input("Digite o diagnostico: ")
    procedimentos = input("Digite os procedimentos: ")
    
    if verificar_dados_tratamento(session, id_paciente, id_fisioterapeuta, data_inicio, data_fim, diagnostico, procedimentos):
        tratamento = criar_tratamento(session, id_paciente, id_fisioterapeuta, data_inicio, data_fim, diagnostico, procedimentos)
        print(f"Tratamento criado com sucesso. ID: {tratamento.ID_Tratamento}")
    else:
        print("Erro ao criar tratamento.")
        
    menu_tratamentos()
    
def menu_editar_tratamento():
    print("\nEditar tratamento")
    id_tratamento = input("Digite o ID do tratamento: ")
    if not id_existe(id_tratamento, 'Tratamento'):
        print("Tratamento nao encontrado.")
    else:
        id_paciente = input("Digite o ID do paciente: ")
        id_fisioterapeuta = input("Digite o ID do fisioterapeuta: ")
        data_inicio = input("Digite a data de inicio do tratamento (AAAA-MM-DD): ")
        data_fim = input("Digite a data de fim do tratamento (AAAA-MM-DD): ")
        diagnostico = input("Digite o diagnostico: ")
        procedimentos = input("Digite os procedimentos: ")
    
        if verificar_dados_tratamento(session, id_paciente, id_fisioterapeuta, data_inicio, data_fim, diagnostico, procedimentos):
            tratamento = session.query(Tratamento).filter(Tratamento.ID_Tratamento == id_tratamento).first()
            tratamento.ID_Paciente = id_paciente
            tratamento.ID_Fisioterapeuta = id_fisioterapeuta
            tratamento.Data_Inicio = data_inicio
            tratamento.Data_Fim = data_fim
            tratamento.Diagnostico = diagnostico
            tratamento.Procedimentos = procedimentos
            session.commit()
            print(f"Tratamento editado com sucesso. ID: {tratamento.ID_Tratamento}")
        else:
            print("Erro ao editar tratamento.")
        
    menu_tratamentos()
    
def menu_excluir_tratamento():
    print("\nExcluir tratamento")
    id_tratamento = input("Digite o ID do tratamento: ")
    if not(id_existe(id_tratamento, 'Tratamento')):
        print("Tratamento nao encontrado.")
    else:
        tratamento = session.query(Tratamento).filter(Tratamento.ID_Tratamento == id_tratamento).first()
        session.delete(tratamento)
        session.commit()
        print(f"Tratamento excluido com sucesso. ID: {id_tratamento}")
    menu_tratamentos()
    
def menu_listar_tratamentos():
    print("\nListar tratamentos")
    tratamentos = session.query(Tratamento).all()
    for tratamento in tratamentos:
        print(f"ID: {tratamento.ID_Tratamento} | ID Paciente: {tratamento.ID_Paciente} | ID Fisioterapeuta: {tratamento.ID_Fisioterapeuta} | Data de Inicio: {tratamento.Data_Inicio} | Data de Fim: {tratamento.Data_Fim} | Diagnostico: {tratamento.Diagnostico} | Procedimentos: {tratamento.Procedimentos}")
    menu_tratamentos()
    
def verificar_dados_tratamento(session, id_paciente, id_fisioterapeuta, data_inicio, data_fim, diagnostico, procedimentos):
    try:
        assert isinstance(id_paciente, int) and id_existe(id_paciente, 'Paciente')
        assert isinstance(id_fisioterapeuta, int) and id_existe(id_fisioterapeuta, 'Fisioterapeuta')
        data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
        data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date()
        assert isinstance(diagnostico, str) and len(diagnostico) <= DIAGNOSTICO_MAX_LENGTH
        assert isinstance(procedimentos, str) and len(procedimentos) <= PROCEDIMENTO_MAX_LENGTH
        
        return True

    except (ValueError, AssertionError) as e:
        session.rollback()
        return None

