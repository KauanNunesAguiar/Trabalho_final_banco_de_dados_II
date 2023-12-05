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
    nome = input("Digite o nome do fisioterapeuta: ")
    especialidade = input("Digite a especialidade do fisioterapeuta: ")
    telefone = input("Digite o telefone do fisioterapeuta: ")
    email = input("Digite o email do fisioterapeuta: ")
    
    if verificar_dados_fisioterapeuta(session, nome, especialidade, telefone, email):
        fisioterapeuta = criar_fisioterapeuta(session, nome, especialidade, telefone, email)
        print(f"Fisioterapeuta criado com sucesso. ID: {fisioterapeuta.ID_Fisioterapeuta}")
    else:
        print("Erro ao criar fisioterapeuta.")
        
    menu_fisioterapeutas()
    
def menu_editar_fisioterapeuta():
    print("\nEditar fisioterapeuta")
    id_fisioterapeuta = input("Digite o ID do fisioterapeuta: ")
    if not id_existe(id_fisioterapeuta, 'Fisioterapeuta'):
        print("Fisioterapeuta nao encontrado.")
    else:
        nome = input("Digite o nome do fisioterapeuta: ")
        especialidade = input("Digite a especialidade do fisioterapeuta: ")
        telefone = input("Digite o telefone do fisioterapeuta: ")
        email = input("Digite o email do fisioterapeuta: ")
    
        if verificar_dados_fisioterapeuta(session, nome, especialidade, telefone, email):
            fisioterapeuta = session.query(Fisioterapeuta).filter(Fisioterapeuta.ID_Fisioterapeuta == id_fisioterapeuta).first()
            fisioterapeuta.Nome = nome
            fisioterapeuta.Especialidade = especialidade
            fisioterapeuta.Telefone = telefone
            fisioterapeuta.Email = email
            session.commit()
            print(f"Fisioterapeuta editado com sucesso. ID: {fisioterapeuta.ID_Fisioterapeuta}")
        else:
            print("Erro ao editar fisioterapeuta.")
        
    menu_fisioterapeutas()
    
def menu_excluir_fisioterapeuta():
    print("\nExcluir fisioterapeuta")
    id_fisioterapeuta = input("Digite o ID do fisioterapeuta: ")
    if not(id_existe(id_fisioterapeuta, 'Fisioterapeuta')):
        print("Fisioterapeuta nao encontrado.")
    else:
        fisioterapeuta = session.query(Fisioterapeuta).filter(Fisioterapeuta.ID_Fisioterapeuta == id_fisioterapeuta).first()
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
    
def verificar_dados_fisioterapeuta(session, nome, especialidade, telefone, email):
    try:
        assert isinstance(nome, str) and len(nome) <= NOME_MAX_LENGTH
        assert isinstance(especialidade, str) and len(especialidade) <= ESPECIALIDADE_MAX_LENGTH
        assert isinstance(telefone, str) and len(telefone) == TELEFONE_MAX_LENGTH
        assert isinstance(email, str) and len(email) <= EMAIL_MAX_LENGTH
        
        return True

    except (ValueError, AssertionError) as e:
        session.rollback()
        return None
    