from menus.inicial import *

opcoes_menu_pacientes = [
    "Criar novo paciente",
    "Editar paciente",
    "Excluir paciente",
    "Listar pacientes"
]

def menu_pacientes():
    opcao = menu(opcoes_menu_pacientes)
    match opcao:
        case 1:
            menu_criar_paciente()
        case 2:
            menu_editar_paciente()
        case 3:
            menu_excluir_paciente()
        case 4:
            menu_listar_pacientes()
        case 5:
            menu_inicial()
        case _:
            print("Opcao invalida. Tente novamente.")
            menu_pacientes()
        
def menu_criar_paciente():
    print("\nCriar novo paciente")
    nome = obter_nome()
    data_nascimento = obter_data_nascimento()
    endereco = obter_endereco()
    telefone = obter_telefone()
    email = obter_email()
    
    if verificar_dados_paciente(session, nome, data_nascimento, endereco, telefone, email):
        paciente = criar_paciente(session, nome, data_nascimento, endereco, telefone, email)
        print(f"Paciente criado com sucesso. ID: {paciente.ID_Paciente}")
    else:
        print("Erro ao criar paciente.")
        
    menu_pacientes()

def menu_editar_paciente():
    print("\nEditar paciente")
    id_paciente = obter_id('Paciente')
    if not id_existe(id_paciente, 'Paciente'):
        print("Paciente nao encontrado.")
    else:
        nome = obter_nome()
        data_nascimento = obter_data_nascimento()
        endereco = obter_endereco()
        telefone = obter_telefone()
        email = obter_email()
    
        if verificar_dados_paciente(session, nome, data_nascimento, endereco, telefone, email):
            paciente = session.query(Paciente).filter(Paciente.ID_Paciente == id_paciente).first()
            paciente.Nome = nome
            paciente.Data_Nascimento = data_nascimento
            paciente.Endereco = endereco
            paciente.Telefone = telefone
            paciente.Email = email
            session.commit()
            print(f"Paciente editado com sucesso. ID: {paciente.ID_Paciente}")
        else:
            print("Erro ao editar paciente.")
        
    menu_pacientes()

def menu_excluir_paciente():
    print("\nExcluir paciente")
    id_paciente = obter_id('Paciente')
    if not(id_existe(id_paciente, 'Paciente')):
        print("Paciente nao encontrado.")
    else:
        paciente = session.query(Paciente).filter(Paciente.ID_Paciente == id_paciente).first()
        
        relatorios_relacionados = session.query(Relatorio).filter_by(ID_Paciente=id_paciente).all()
        for relatorio in relatorios_relacionados:
            session.delete(relatorio)
        
        pagamentos_relacionados = session.query(Pagamento).filter_by(ID_Paciente=id_paciente).all()
        for pagamento in pagamentos_relacionados:
            session.delete(pagamento)
            
        agendamentos_relacionados = session.query(Agendamento).filter_by(ID_Paciente=id_paciente).all()
        for agendamento in agendamentos_relacionados:
            session.delete(agendamento)
            
        historicos_relacionados = session.query(HistoricoMedico).filter_by(ID_Paciente=id_paciente).all()
        for historico in historicos_relacionados:
            session.delete(historico)
            
        tratamentos_relacionados = session.query(Tratamento).filter_by(ID_Paciente=id_paciente).all()
        for tratamento in tratamentos_relacionados:
            session.delete(tratamento)
            
        session.delete(paciente)
        session.commit()
        print(f"Paciente excluido com sucesso. ID: {id_paciente}")
    menu_pacientes()

def menu_listar_pacientes():
    print("\nListar pacientes")
    pacientes = session.query(Paciente).all()
    for paciente in pacientes:
        print(f"ID: {paciente.ID_Paciente} | Nome: {paciente.Nome} | Data de Nascimento: {paciente.Data_Nascimento} | Endereco: {paciente.Endereco} | Telefone: {paciente.Telefone} | Email: {paciente.Email}")
    menu_pacientes()
    
def verificar_dados_paciente(session, nome, data_nascimento, endereco, telefone, email):
    try:
        assert isinstance(nome, str) and len(nome) <= NOME_MAX_LENGTH
        data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        assert isinstance(endereco, str) and len(endereco) <= ENDERECO_MAX_LENGTH
        assert isinstance(telefone, str) and len(telefone) <= TELEFONE_MAX_LENGTH
        assert isinstance(email, str) and len(email) <= EMAIL_MAX_LENGTH
        
        return True

    except (ValueError, AssertionError) as e:
        session.rollback()
        return None
