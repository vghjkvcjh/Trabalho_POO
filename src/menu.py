import os
from modelos.sistema import Sistema

# Função para limpar o terminal
def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função do menu principal
def menu_principal():
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
                menu_criarCliente()
            elif opcao == 2:
                limpa()
                
            elif opcao == 3:
                limpa()
                return  # Retorna ao menu principal

        except ValueError as erro:
            limpa()
            print(f"Erro: {erro}\n")

# Chama a função do menu principal / inicia o menu
menu_principal()