from menus.inicial import *

opcoes_menu_usuarios = [
    "Criar novo usuario",
    "Editar usuario",
    "Excluir usuario",
    "Listar usuarios"
]

def menu_usuarios():
    opcao = menu(opcoes_menu_usuarios)
    match opcao:
        case 1:
            menu_criar_usuario()
        case 2:
            menu_editar_usuario()
        case 3:
            menu_excluir_usuario()
        case 4:
            menu_listar_usuarios()
        case 5:
            menu_inicial()
        case _:
            print("Opcao invalida. Tente novamente.")
            menu_usuarios()

def menu_criar_usuario():
    print("\nCriar novo usuario")
    nome = obter_nome()
    username = input("Digite o username do usuario: ")
    senha = input("Digite a senha do usuario: ")
    nivel_acesso = obter_nivel_acesso()
    
    if verificar_dados_usuario(session, nome, username, senha, nivel_acesso):
        usuario = criar_usuario(session, nome, username, senha, nivel_acesso)
        print(f"Usuario criado com sucesso. ID: {usuario.ID_Usuario}")
    else:
        print("Erro ao criar usuario.")
        
    menu_usuarios()
    
def menu_editar_usuario():
    print("\nEditar usuario")
    id_usuario = obter_id('Usuario')
    nome = obter_nome()
    username = input("Digite o username do usuario: ")
    senha = input("Digite a senha do usuario: ")
    nivel_acesso = obter_nivel_acesso()

    if verificar_dados_usuario(session, nome, username, senha):
        usuario = session.query(Usuario).filter(Usuario.ID_Usuario == id_usuario).first()
        usuario.Nome = nome
        usuario.Username = username
        usuario.Senha = senha
        usuario.Nivel_Acesso = nivel_acesso
        session.commit()
        
        print(f"Usuario editado com sucesso. ID: {usuario.ID_Usuario}")
    else:
        print("Erro ao editar usuario.")
        
    menu_usuarios()
    
def retornar_nivel_acesso(nivel_acesso):
    if nivel_acesso == 'V':
        return 'Visitante'
    elif nivel_acesso == 'B':
        return 'Basico'
    elif nivel_acesso == 'A':
        return 'Avancado'
    else:
        return 'Nivel de acesso invalido'
    
def menu_excluir_usuario():
    print("\nExcluir usuario")
    id_usuario = obter_id('Usuario')
    if not(id_existe(id_usuario, 'Usuario')):
        print("Usuario nao encontrado.")
    else:
        usuario = session.query(Usuario).filter(Usuario.ID_Usuario == id_usuario).first()
        session.delete(usuario)
        session.commit()
        print(f"Usuario excluido com sucesso. ID: {id_usuario}")
    menu_usuarios()
    
def menu_listar_usuarios():
    print("\nListar usuarios")
    usuarios = session.query(Usuario).all()
    for usuario in usuarios:
        print(f"ID: {usuario.ID_Usuario} | Nome: {usuario.Nome} | Username: {usuario.Username} | Senha: {usuario.Senha} | Nivel de Acesso: {retornar_nivel_acesso(usuario.Nivel_Acesso)}")
    menu_usuarios()
    
def verificar_dados_usuario(session, nome, username, senha, nivel_acesso):
    try:
        assert isinstance(nome, str) and len(nome) <= NOME_MAX_LENGTH
        assert isinstance(username, str) and len(username) <= USERNAME_MAX_LENGTH
        assert isinstance(senha, str) and len(senha) <= SENHA_MAX_LENGTH
        assert isinstance(nivel_acesso, str) and (nivel_acesso == 'V' or nivel_acesso == 'B' or nivel_acesso == 'A') 
        
        return True

    except (ValueError, AssertionError) as e:
        session.rollback()
        return None
    