import os
from modelos.evento import Evento
from modelos.organizador import Organizador
from modelos.cliente import Cliente

def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    limpa()

    while True:
        print("Bem-vindo lorem ipsum!")
        print("-----------------------")
        print("1. Entrar")
        print("2. Criar conta")
        print("3. Sair")
        print("-----------------------")

        try:
            opcao = int(input("Digite uma opção: "))
            
            if opcao not in [1, 2, 3]:
                raise ValueError("Número de opção inválido!")
            
            if opcao == 1:
                limpa()
                print("Entrando\n")
            elif opcao == 2:
                limpa()
                print("Criando\n")
            elif opcao == 3:
                print("\nAdeus!\n")
                break

        except ValueError as erro:
            limpa()
            print(f"Erro: {erro}\n")

menu_principal()