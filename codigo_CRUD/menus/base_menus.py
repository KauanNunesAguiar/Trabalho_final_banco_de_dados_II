from banco_de_dados.funcoes_tabelas import *

# Definir funcoes para melhorar a interacao com o usuario
def menu(opcoes):
    while True:
        print("\nEscolha uma das opcoes abaixo:")
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i} - {opcao}")

        print(f"{len(opcoes) + 1} - Voltar")
        escolha = input("Digite sua opcao: ")

        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(opcoes) + 1:
                return escolha
            else:
                print("Opcao invalida. Tente novamente.")
        except ValueError:
            print("Digite um numero valido.")
            
def id_existe(id, tabela):
    try:
        model_class = globals()[tabela]
        return session.query(model_class).filter(getattr(model_class, f'ID_{tabela}') == id).first()
    except KeyError:
        return None
    
def obter_nome_id(id, tabela):
    try:
        model_class = globals()[tabela]
        return session.query(model_class).filter(getattr(model_class, f'ID_{tabela}') == id).first().Nome
    except KeyError:
        return None
    
# Função genérica para obter um ID de uma tabela
def obter_id(tabela):
    while True:
        try:
            id_valor = int(input(f"Digite o ID do {tabela.lower()}: "))
            if not id_existe(id_valor, tabela):
                print(f"ID de {tabela.lower()} não existe. Tente novamente.")
                continue
            return id_valor
        except ValueError:
            print("Entrada inválida. Certifique-se de fornecer um valor inteiro.")

# Função genérica para obter data e hora
def obter_data_hora():
    while True:
        try:
            data_hora = input("Digite a data e hora (AAAA-MM-DD HH:MM:SS): ")
            datetime.strptime(data_hora, "%Y-%m-%d %H:%M:%S")
            return data_hora
        except ValueError:
            print("Formato de data e hora inválido. Tente novamente.")

# Função genérica para obter tempos
def obter_tempo():
    while True:
        try:
            duracao = input("Digite a duração: ")
            datetime.strptime(duracao, "%H:%M:%S")
            return duracao
        except ValueError:
            print("Formato de duração inválido. Tente novamente.")
           
# Funções genérica para obter datas
def obter_data():
    while True:
        try:
            data = input("Digite a data (AAAA-MM-DD): ")
            datetime.strptime(data, "%Y-%m-%d")
            return data
        except ValueError:
            print("Formato de data inválido. Tente novamente.")
            
def obter_data_nascimento():
    while True:
        try:
            data_nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
            datetime.strptime(data_nascimento, "%Y-%m-%d")
            return data_nascimento
        except ValueError:
            print("Formato de data inválido. Tente novamente.")

def obter_nivel_acesso():
    while True:
        nivel_acesso = input("Digite o nivel de acesso: ")
        if nivel_acesso == 'V' or nivel_acesso == 'B' or nivel_acesso == 'A':
            return nivel_acesso
        else:
            print(f"Nivel de acesso inválido. Tente novamente.")
            
def obter_conteudo():
    while True:
        conteudo = input("Digite o conteudo: ")
        if len(conteudo) <= CONTEUDO_MAX_LENGTH:
            return conteudo
        else:
            print(f"Conteudo deve ter no máximo {CONTEUDO_MAX_LENGTH} caracteres. Tente novamente.")
        
def obter_data_inicio():
    while True:
        try:
            data_inicio = input("Digite a data de inicio (AAAA-MM-DD): ")
            datetime.strptime(data_inicio, "%Y-%m-%d")
            return data_inicio
        except ValueError:
            print("Formato de data inválido. Tente novamente.")

def obter_data_fim():
    while True:
        try:
            data_fim = input("Digite a data de fim (AAAA-MM-DD): ")
            datetime.strptime(data_fim, "%Y-%m-%d")
            return data_fim
        except ValueError:
            print("Formato de data inválido. Tente novamente.")
 
def obter_metodo_pagamento():
    while True:
        metodo_pagamento = input("Digite o metodo de pagamento: ")
        if metodo_pagamento == 'C' or metodo_pagamento == 'D' or metodo_pagamento == 'E' or metodo_pagamento == 'P':
            return metodo_pagamento
        else:
            print(f"Método de pagamento inválido. Tente novamente.")

# Função genérica para obter nomes
def obter_nome():
    while True:
        nome = input("Digite o nome: ")
        if len(nome) <= NOME_MAX_LENGTH:
            return nome
        else:
            print(f"Nome deve ter no máximo {NOME_MAX_LENGTH} caracteres. Tente novamente.")

# Função genérica para obter valor de pagamentos
def obter_valor():
    while True:
        try:
            valor = float(input("Digite o valor: "))
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")
            
# Função genérica para obter procedimentos
def obter_procedimentos():
    while True:
        procedimentos = input("Digite os procedimentos: ")
        if len(procedimentos) <= PROCEDIMENTO_MAX_LENGTH:
            return procedimentos
        else:
            print(f"Procedimentos devem ter no máximo {PROCEDIMENTO_MAX_LENGTH} caracteres. Tente novamente.")

# funcao generica para obter diagnóstico
def obter_diagnostico():
    while True:
        diagnostico = input("Digite o diagnóstico: ")
        if len(diagnostico) <= DIAGNOSTICO_MAX_LENGTH:
            return diagnostico
        else:
            print(f"Diagnóstico deve ter no máximo {DIAGNOSTICO_MAX_LENGTH} caracteres. Tente novamente.")

# Função genérica para obter descrições
def obter_descricao():
    while True:
        descricao = input("Digite a descrição: ")
        if len(descricao) <= DESCRICAO_MAX_LENGTH:
            return descricao
        else:
            print(f"Descrição deve ter no máximo {DESCRICAO_MAX_LENGTH} caracteres. Tente novamente.")

# Função genérica para obter Telefone
def obter_telefone():
    while True:
        telefone = input("Digite o telefone: ")
        if len(telefone) == TELEFONE_MAX_LENGTH:
            return telefone
        else:
            print(f"Telefone exatamente {TELEFONE_MAX_LENGTH} caracteres. Tente novamente.")

# Função genérica para obter tratamento anterior
def obter_tratamento_anterior():
    while True:
        tratamento_anterior = input("Digite o tratamento anterior: ")
        if len(tratamento_anterior) <= TRATAMENTO_ANTERIOR_MAX_LENGTH:
            return tratamento_anterior
        else:
            print(f"Tratamento anterior deve ter no máximo {TRATAMENTO_ANTERIOR_MAX_LENGTH} caracteres. Tente novamente.")

# Função genérica para obter e-mails
def obter_email():
    while True:
        email = input("Digite o e-mail: ")
        if len(email) <= EMAIL_MAX_LENGTH:
            return email
        else:
            print(f"E-mail deve ter no máximo {EMAIL_MAX_LENGTH} caracteres. Tente novamente.")
            
# Função genérica para obter endereços
def obter_endereco():
    while True:
        endereco = input("Digite o endereço: ")
        if len(endereco) <= ENDERECO_MAX_LENGTH:
            return endereco
        else:
            print(f"Endereço deve ter no máximo {ENDERECO_MAX_LENGTH} caracteres. Tente novamente.")

# Função genérica para obter especialidades
def obter_especialidade():
    while True:
        especialidade = input("Digite a especialidade: ")
        if len(especialidade) <= ESPECIALIDADE_MAX_LENGTH:
            return especialidade
        else:
            print(f"Especialidade deve ter no máximo {ESPECIALIDADE_MAX_LENGTH} caracteres. Tente novamente.")
            
# Função genérica para obter observações
def obter_observacoes():
    while True:
        observacoes = input("Digite as observações: ")
        if len(observacoes) <= OBSERVACOES_MAX_LENGTH:
            return observacoes
        else:
            print(f"Observações devem ter no máximo {OBSERVACOES_MAX_LENGTH} caracteres. Tente novamente.")

            