from menus.inicial import *

opcoes_menu_agendamentos = [
    "Criar novo agendamento",
    "Editar agendamento",
    "Excluir agendamento",
    "Listar agendamentos"
]

def menu_agendamentos():
    opcao = menu(opcoes_menu_agendamentos)
    match opcao:
        case 1:
            menu_criar_agendamento()
        case 2:
            menu_editar_agendamento()
        case 3:
            menu_excluir_agendamento()
        case 4:
            menu_listar_agendamentos()
        case 5:
            menu_inicial()
        case _:
            print("Opcao invalida. Tente novamente.")
            menu_agendamentos()

def menu_criar_agendamento():
    print("\nCriar novo agendamento")
    id_paciente = obter_id('Paciente')
    id_fisioterapeuta = obter_id('Fisioterapeuta')
    data_hora = obter_data_hora()
    duracao = obter_tempo()
    observacoes = obter_observacoes()
    
    if verificar_dados_agendamento(session, id_paciente, id_fisioterapeuta, data_hora, duracao, observacoes):
        agendamento = criar_agendamento(session, id_paciente, id_fisioterapeuta, data_hora, duracao, observacoes)
        print(f"Agendamento criado com sucesso. ID: {agendamento.ID_Agendamento}")
    else:
        print("Erro ao criar agendamento.")
        
    menu_agendamentos()

def menu_editar_agendamento():
    print("\nEditar agendamento")
    id_agendamento = obter_id('Agendamento')
    
    try:
        id_paciente = obter_id('Paciente')
        id_fisioterapeuta = obter_id('Fisioterapeuta')
        data_hora = obter_data_hora()
        duracao = obter_tempo()
        observacoes = obter_observacoes()

        if verificar_dados_agendamento(session, id_paciente, id_fisioterapeuta, data_hora, duracao, observacoes):
            agendamento = session.query(Agendamento).filter(Agendamento.ID_Agendamento == id_agendamento).first()
            agendamento.ID_Paciente = id_paciente
            agendamento.ID_Fisioterapeuta = id_fisioterapeuta
            agendamento.Data_Hora = data_hora
            agendamento.Duracao = duracao
            agendamento.Observacoes = observacoes
            session.commit()
            print(f"Agendamento editado com sucesso. ID: {agendamento.ID_Agendamento}")
        else:
            print("Erro ao editar agendamento.")
    except ValueError:
        print("Entrada inválida. Certifique-se de fornecer valores inteiros para IDs.")
    
    menu_agendamentos()

def menu_excluir_agendamento():
    print("\nExcluir agendamento")
    id_agendamento = obter_id('Agendamento')
    if not(id_existe(id_agendamento, 'Agendamento')):
        print("Agendamento nao encontrado.")
    else:
        agendamento = session.query(Agendamento).filter(Agendamento.ID_Agendamento == id_agendamento).first()
        session.delete(agendamento)
        session.commit()
        print(f"Agendamento excluido com sucesso. ID: {id_agendamento}")
    menu_agendamentos()

def menu_listar_agendamentos():
    print("\nListar agendamentos")
    agendamentos = session.query(Agendamento).all()
    for agendamento in agendamentos:
        print(f"ID: {agendamento.ID_Agendamento} | ID Paciente: {agendamento.ID_Paciente} | ID Fisioterapeuta: {agendamento.ID_Fisioterapeuta} | Data e Hora: {agendamento.Data_Hora} | Duracao: {agendamento.Duracao} | Observacoes: {agendamento.Observacoes}")
    menu_agendamentos()

def verificar_dados_agendamento(session, id_paciente, id_fisioterapeuta, data_hora, duracao, observacoes):
    try:
        assert isinstance(id_paciente, int) and id_existe(id_paciente, 'Paciente')
        assert isinstance(id_fisioterapeuta, int) and id_existe(id_fisioterapeuta, 'Fisioterapeuta')
        data_hora = datetime.strptime(data_hora, "%Y-%m-%d %H:%M:%S")
        duracao = datetime.strptime(duracao, "%H:%M:%S").time()
        assert isinstance(observacoes, str) and len(observacoes) <= OBSERVACOES_MAX_LENGTH
        
        return True

    except ValueError as e:
        session.rollback()
        return False
    except AssertionError as e:
        session.rollback()
        return False
