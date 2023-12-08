from menus.base_menus import *

opcoes_menu_inicial = [
    "Acessar tabela de pacientes",
    "Acessar tabela de fisioterapeutas",
    "Acessar tabela de usuarios",
    "Acessar tabela de agendamentos",
    "Acessar tabela de historico medico",
    "Acessar tabela de tratamentos",
    "Acessar tabela de pagamentos",
    "Acessar tabela de relatorios",
]

def menu_inicial():
    return menu(opcoes_menu_inicial)