from menus.inicial import menu_inicial
from menus.paciente import menu_pacientes
from menus.fisioterapeuta import menu_fisioterapeutas
from menus.usuario import menu_usuarios
from menus.agendamento import menu_agendamentos
from menus.historico_medico import menu_historico_medico
from menus.tratamento import menu_tratamentos
from menus.pagamento import menu_pagamentos
from menus.relatorio import menu_relatorios
    
def main():
    while True:
        menu_opcao = menu_inicial()
        
        match menu_opcao:
            case 1:
                menu_pacientes()
            case 2:
                menu_fisioterapeutas()
            case 3:
                menu_usuarios()
            case 4:
                menu_agendamentos()
            case 5:
                menu_historico_medico()
            case 6:
                menu_tratamentos()
            case 7:
                menu_pagamentos()
            case 8:
                menu_relatorios()
            case 9:
                print("Saindo do programa...")
                exit()
            case _:
                print("Opcao invalida. Tente novamente.")
main()
