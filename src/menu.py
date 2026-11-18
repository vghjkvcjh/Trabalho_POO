import os
from modelos.sistema import Sistema

def limpa(): # Função para limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_principal(): # Função do menu principal
    limpa()
    sistema = Sistema()

    while True: # Loop principal do menu
        print("=======================")
        print("Bem-vindo lorem ipsum!")
        print("-----------------------")
        print("1. Entrar")
        print("2. Criar conta")
        print("3. Sair")
        print("=======================")

        try: # Loop para capturar a opção do usuário
            opcao = int(input("Digite uma opção: "))

            if opcao not in [1, 2, 3]: # Levanta uma exceção se a opção for inválida
                raise ValueError("Número de opção inválido!")
            
            if opcao == 1: # Chama a função de login
                limpa()
                menu_login(sistema)
                
            elif opcao == 2: # Chama a função de criação de conta
                menu_criarConta(sistema)
            elif opcao == 3: # Sai do programa
                limpa()
                print("Adeus!\n")
                break

        except ValueError as erro: # Tratamento de exceção para entrada inválida
            limpa()
            print(f"Erro: {erro}\n") # Exibe a mensagem de erro


def menu_login(sistema):
    limpa()

    while True:
        print("=======================")
        print("Login")
        print("-----------------------")
        print("1. Entrar")
        print("2. Voltar ao menu principal")
        print("=======================")

        try:
            opcao = int(input("Digite uma opção: "))

            if opcao not in [1, 2]:
                raise ValueError("Número de opção inválido!")

            if opcao == 1:
                limpa()
                cpf = int(input("Digite o CPF: "))
                senha = input("Digite a senha: ")

                try:
                    pessoa = sistema.Login(cpf, senha)
                    limpa()
                    print(f"Bem-vindo(a), {pessoa.nome}!\n")
                    return
                
                except ValueError as erro:
                    limpa()
                    print(f"Erro: {erro}\n")

            elif opcao == 2:
                limpa()
                return

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
                menu_criarOrganizador(sistema)
                
            elif opcao == 3:
                limpa()
                return

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
                cpf = int(input("Digite o CPF: "))
                idade = int(input("Digite a idade: "))
                senha = input("Digite a senha: ")
                
                sistema.criarCliente(nome, cpf, idade, senha)

                limpa()

                print("Conta de usuário criada com sucesso!\n")
                return
                
            elif opcao == 2:
                limpa()
                return

        except ValueError as erro:
            limpa()
            print(f"Erro: {erro}\n")

def menu_criarOrganizador(sistema):
    limpa()

    while True:
        print("=======================")
        print("Criar Conta de Organizador")
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
                cpf = int(input("Digite o CPF: "))
                idade = int(input("Digite a idade: "))
                senha = input("Digite a senha: ")
                
                sistema.criarOrganizador(nome, cpf, idade, senha)

                limpa()

                menu_login(sistema)
                return
                
            elif opcao == 2:
                limpa()
                return

        except ValueError as erro:
            limpa()
            print(f"Erro: {erro}\n")



# Chama a função do menu principal / inicia o menu
menu_principal()