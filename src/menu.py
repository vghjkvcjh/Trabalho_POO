import os
from modelos.evento import Evento
from modelos.organizador import Organizador
from modelos.cliente import Cliente

# Função para limpar o terminal
def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função do menu principal
def menu_principal():
    limpa()

    # Loop principal do menu
    while True:
        print("Bem-vindo lorem ipsum!")
        print("-----------------------")
        print("1. Entrar")
        print("2. Criar conta")
        print("3. Sair")
        print("-----------------------")

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
                limpa()
                print("Criando\n")
            elif opcao == 3:
                limpa()
                print("Adeus!\n")
                break

        # Tratamento de exceção para entrada inválida
        except ValueError as erro:
            limpa()
            print(f"Erro: {erro}\n")

# Chama a função do menu principal / inicia o menu
menu_principal()