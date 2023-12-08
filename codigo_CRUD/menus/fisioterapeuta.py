from menus.inicial import *

opcoes_menu_fisioterapeutas = [
    "Criar novo fisioterapeuta",
    "Editar fisioterapeuta",
    "Excluir fisioterapeuta",
    "Listar fisioterapeutas"
]

def menu_fisioterapeutas():
    opcao = menu(opcoes_menu_fisioterapeutas)
    match opcao:
        case 1:
            menu_criar_fisioterapeuta()
        case 2:
            menu_editar_fisioterapeuta()
        case 3:
            menu_excluir_fisioterapeuta()
        case 4:
            menu_listar_fisioterapeutas()
        case 5:
            menu_inicial()
        case _:
            print("Opcao invalida. Tente novamente.")
            menu_fisioterapeutas()

def menu_criar_fisioterapeuta():
    print("\nCriar novo fisioterapeuta")
    nome = obter_nome()
    especialidade = obter_especialidade()
    telefone = obter_telefone()
    email = obter_email()

    if verificar_dados_fisioterapeuta(nome, especialidade, telefone, email):
        fisioterapeuta = criar_fisioterapeuta(session, nome, especialidade, telefone, email)
        print(f"Fisioterapeuta criado com sucesso. ID: {fisioterapeuta.ID_Fisioterapeuta}")
    else:
        print("Erro ao criar fisioterapeuta.")

    menu_fisioterapeutas()

def menu_editar_fisioterapeuta():
    print("\nEditar fisioterapeuta")
    id_fisioterapeuta = obter_id('Fisioterapeuta')

    try:
        nome = obter_nome()
        especialidade = obter_especialidade()
        telefone = obter_telefone()
        email = obter_email()

        if verificar_dados_fisioterapeuta(nome, especialidade, telefone, email):
            fisioterapeuta = session.query(Fisioterapeuta).filter(Fisioterapeuta.ID_Fisioterapeuta == id_fisioterapeuta).first()
            fisioterapeuta.Nome = nome
            fisioterapeuta.Especialidade = especialidade
            fisioterapeuta.Telefone = telefone
            fisioterapeuta.Email = email
            session.commit()
            print(f"Fisioterapeuta editado com sucesso. ID: {fisioterapeuta.ID_Fisioterapeuta}")
        else:
            print("Erro ao editar fisioterapeuta.")
    except ValueError:
        print("Entrada inválida. Certifique-se de fornecer valores inteiros para IDs.")

    menu_fisioterapeutas()

def menu_excluir_fisioterapeuta():
    print("\nExcluir fisioterapeuta")
    id_fisioterapeuta = obter_id('Fisioterapeuta')
    if not id_existe(id_fisioterapeuta, 'Fisioterapeuta'):
        print("Fisioterapeuta nao encontrado.")
    else:
        fisioterapeuta = session.query(Fisioterapeuta).filter(Fisioterapeuta.ID_Fisioterapeuta == id_fisioterapeuta).first()
            
        agendamentos_relacionados = session.query(Agendamento).filter_by(ID_Fisioterapeuta=id_fisioterapeuta).all()
        for agendamento in agendamentos_relacionados:
            session.delete(agendamento)
            
        tratamentos_relacionados = session.query(Tratamento).filter_by(ID_Paciente=id_fisioterapeuta).all()
        for tratamento in tratamentos_relacionados:
            session.delete(tratamento)
            
        session.delete(fisioterapeuta)
        session.commit()
        print(f"Fisioterapeuta excluido com sucesso. ID: {id_fisioterapeuta}")
    menu_fisioterapeutas()

def menu_listar_fisioterapeutas():
    print("\nListar fisioterapeutas")
    fisioterapeutas = session.query(Fisioterapeuta).all()
    for fisioterapeuta in fisioterapeutas:
        print(f"ID: {fisioterapeuta.ID_Fisioterapeuta} | Nome: {fisioterapeuta.Nome} | Especialidade: {fisioterapeuta.Especialidade} | Telefone: {fisioterapeuta.Telefone} | Email: {fisioterapeuta.Email}")
    menu_fisioterapeutas()

def verificar_dados_fisioterapeuta(nome, especialidade, telefone, email):
    try:
        assert isinstance(nome, str) and len(nome) <= NOME_MAX_LENGTH
        assert isinstance(especialidade, str) and len(especialidade) <= ESPECIALIDADE_MAX_LENGTH
        assert isinstance(telefone, str) and len(telefone) == TELEFONE_MAX_LENGTH
        assert isinstance(email, str) and len(email) <= EMAIL_MAX_LENGTH

        return True

    except AssertionError:
        session.rollback()
        return False
