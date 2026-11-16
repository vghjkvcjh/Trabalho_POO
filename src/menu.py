import os
from modelos.sistema import Sistema

# Função para limpar o terminal
def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função do menu principal
def menu_principal() -> None:
    limpa()
    sistema = Sistema()

    # Loop principal do menu
    while True:
        print("=======================")
        print("Bem-vindo lorem ipsum!")
        print("-----------------------")
        print("1. Entrar")
        print("2. Criar conta")
        print("3. Sair")
        print("=======================")

        # Loop para capturar a opção do usuário
        try:
            opcao = int(input("Digite uma opção: "))

            # Levanta uma exceção se a opção for inválida
            if opcao not in [1, 2, 3]:
                raise ValueError("Número de opção inválido!")
            
            if opcao == 1:
                limpa()
                print("Entrando\n")
            elif opcao == 2:
                menu_criarConta(sistema)
            elif opcao == 3:
                limpa()
                print("Adeus!\n")
                break

        # Tratamento de exceção para entrada inválida
        except ValueError as erro:
            limpa()
            print(f"Erro: {erro}\n")


def menu_criarConta(sistema):
    limpa()

    while True:
        print("=======================")
        print("Criar Conta")
        print("-----------------------")
        print("1. Criar conta de usuário")
        print("2. Criar conta de organizador")
        print("3. Voltar ao menu principal")
        print("=======================")

        try:
            opcao = int(input("Digite uma opção: "))

            if opcao not in [1, 2, 3]:
                raise ValueError("Número de opção inválido!")

            if opcao == 1:
                limpa()
                menu_criarCliente(sistema)
            elif opcao == 2:
                limpa()
                
            elif opcao == 3:
                limpa()
                return  # Retorna ao menu principal

        except ValueError as erro:
            limpa()
            print(f"Erro: {erro}\n")


def menu_criarCliente(sistema):
    limpa()

    while True:
        print("=======================")
        print("Criar Conta de Usuário")
        print("-----------------------")
        print("1. Criar conta")
        print("2. Voltar ao menu anterior")
        print("=======================")

        try:
            opcao = int(input("Digite uma opção: "))

            if opcao not in [1, 2]:
                raise ValueError("Número de opção inválido!")

            if opcao == 1:
                limpa()
                
                nome = input("Digite o nome: ")
                cpf = input("Digite o CPF: ")
                idade = int(input("Digite a idade: "))
                senha = input("Digite a senha: ")
                
                sistema.criarCliente(nome, cpf, idade, senha)

                limpa()

                print("Conta de usuário criada com sucesso!\n")
                return  # Retorna ao menu anterior
                
            elif opcao == 2:
                limpa()
                return  # Retorna ao menu anterior

        except ValueError as erro:
            limpa()
            print(f"Erro: {erro}\n")

# Chama a função do menu principal / inicia o menu
menu_principal()