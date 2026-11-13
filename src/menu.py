import os
from modelos.evento import Evento
from modelos.organizador import Organizador
from modelos.cliente import Cliente

os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        print("Bem-vindo lorem ipsum!")
        print("-----------------------")
        print("1. Entrar")
        print("2. Criar conta")
        print("3. Sair")
        print("-----------------------")

        try:
            opcao = int(input("Digite uma opção: "))

            if opcao == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Entrando\n")
            elif opcao == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Criando\n")
            elif opcao == 3:
                print("\nAdeus!\n")
                break

            if opcao not in [1, 2, 3]:
                raise ValueError

        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Digite uma opção válida.\n")

menu_principal()