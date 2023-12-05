from menus.inicial import *

opcoes_menu_historico_medico = [
    "Criar novo historico medico",
    "Editar historico medico",
    "Excluir historico medico",
    "Listar historicos medicos"
]

def menu_historico_medico():
    opcao = menu(opcoes_menu_historico_medico)
    match opcao:
        case 1:
            menu_criar_historico_medico()
        case 2:
            menu_editar_historico_medico()
        case 3:
            menu_excluir_historico_medico()
        case 4:
            menu_listar_historico_medico()
        case 5:
            menu_inicial()
        case _:
            print("Opcao invalida. Tente novamente.")
            menu_historico_medico()

def menu_criar_historico_medico():
    print("\nCriar novo historico medico")
    id_paciente = input("Digite o ID do paciente: ")
    data_consulta = input("Digite a data da consulta (AAAA-MM-DD): ")
    diagnostico = input("Digite o diagnostico: ")
    tratamento_anterior = input("Digite o tratamento anterior: ")
    
    if verificar_dados_historico_medico(session, id_paciente, data_consulta, diagnostico, tratamento_anterior):
        historico_medico = criar_historico_medico(session, id_paciente, data_consulta, diagnostico, tratamento_anterior)
        print(f"Historico medico criado com sucesso. ID: {historico_medico.ID_HistoricoMedico}")
    else:
        print("Erro ao criar historico medico.")
        
    menu_historico_medico()
    
def menu_editar_historico_medico():
    print("\nEditar historico medico")
    id_historico_medico = input("Digite o ID do historico medico: ")
    if not id_existe(id_historico_medico, 'HistoricoMedico'):
        print("Historico medico nao encontrado.")
    else:
        id_paciente = input("Digite o ID do paciente: ")
        data_consulta = input("Digite a data da consulta (AAAA-MM-DD): ")
        diagnostico = input("Digite o diagnostico: ")
        tratamento_anterior = input("Digite o tratamento anterior: ")
    
        if verificar_dados_historico_medico(session, id_paciente, data_consulta, diagnostico, tratamento_anterior):
            historico_medico = session.query(HistoricoMedico).filter(HistoricoMedico.ID_HistoricoMedico == id_historico_medico).first()
            historico_medico.ID_Paciente = id_paciente
            historico_medico.DataConsulta = data_consulta
            historico_medico.Diagnostico = diagnostico
            historico_medico.TratamentoAnterior = tratamento_anterior
            session.commit()
            print(f"Historico medico editado com sucesso. ID: {historico_medico.ID_HistoricoMedico}")
        else:
            print("Erro ao editar historico medico.")
        
    menu_historico_medico()
    
def menu_excluir_historico_medico():
    print("\nExcluir historico medico")
    id_historico_medico = input("Digite o ID do historico medico: ")
    if not(id_existe(id_historico_medico, 'HistoricoMedico')):
        print("Historico medico nao encontrado.")
    else:
        historico_medico = session.query(HistoricoMedico).filter(HistoricoMedico.ID_HistoricoMedico == id_historico_medico).first()
        session.delete(historico_medico)
        session.commit()
        print(f"Historico medico excluido com sucesso. ID: {id_historico_medico}")
    menu_historico_medico()
    
def menu_listar_historico_medico():
    print("\nListar historicos medicos")
    historicos_medicos = session.query(HistoricoMedico).all()
    for historico_medico in historicos_medicos:
        print(f"ID: {historico_medico.ID_HistoricoMedico} | ID Paciente: {historico_medico.ID_Paciente} | Data da Consulta: {historico_medico.DataConsulta} | Diagnostico: {historico_medico.Diagnostico} | Tratamento Anterior: {historico_medico.TratamentoAnterior}")
    menu_historico_medico()
    
def verificar_dados_historico_medico(session, id_paciente, data_consulta, diagnostico, tratamento_anterior):
    try:
        assert isinstance(id_paciente, int) and id_existe(id_paciente, 'Paciente')
        data_consulta = datetime.strptime(data_consulta, "%Y-%m-%d").date()
        assert isinstance(diagnostico, str) and len(diagnostico) <= DIAGNOSTICO_MAX_LENGTH
        assert isinstance(tratamento_anterior, str) and len(tratamento_anterior) <= TRATAMENTO_ANTERIOR_MAX_LENGTH
        
        return True

    except (ValueError, AssertionError) as e:
        session.rollback()
        return None