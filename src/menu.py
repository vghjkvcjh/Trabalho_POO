import os
from datetime import datetime

from modelos.sistema import Sistema
from modelos.cliente import Cliente
from modelos.organizador import Organizador


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

                    if isinstance(pessoa, Cliente):
                        menu_cliente(sistema, pessoa)
                    elif isinstance(pessoa, Organizador):
                        menu_organizador(pessoa)

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
                cpf = (input("Digite o CPF: "))
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
                cpf = input("Digite o CPF: ")
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


def listar_eventos(eventos):
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    for evento in eventos:
        print(f"ID: {evento.id_ev} | {evento}")
        print("-----------------------------------")


def buscar_evento(eventos):
    if not eventos:
        print("Nenhum evento disponível.")
        return None

    try:
        id_evento = int(input("Digite o ID do evento: "))
    except ValueError:
        print("O ID precisa ser um número.")
        return None

    for evento in eventos:
        if evento.id_ev == id_evento:
            return evento

    print("Evento não encontrado.")
    return None


def menu_cliente(sistema, cliente):
    limpa()

    while True:
        limpa()
        print("=======================")
        print(f"Olá, {cliente.nome}!")
        print("-----------------------")
        print("1. Ver eventos / participar")
        print("2. Ver meus ingressos")
        print("3. Sair da conta")
        print("=======================")

        try:
            opcao = int(input("Digite uma opção: "))

            if opcao not in [1, 2, 3]:
                raise ValueError("Número de opção inválido!")

            if opcao == 1:
                tela_eventos_cliente(sistema, cliente)

            elif opcao == 2:
                limpa()
                print("========== MEUS INGRESSOS ==========")

                if not cliente.ingressosP:
                    print("Você ainda não possui ingressos.")
                else:
                    for ingresso in cliente.ingressosP:
                        print(ingresso)

                input("\nPressione ENTER para continuar...")

            elif opcao == 3:
                return

        except ValueError as erro:
            print(f"Erro: {erro}")
            input("\nPressione ENTER para continuar...")


def tela_eventos_cliente(sistema, cliente):
    limpa()

    while True:
        limpa()
        print("========== EVENTOS DISPONÍVEIS ==========")
        eventos = sistema.ListarEventos()
        listar_eventos(eventos)
        print("Digite o ID de um evento para participar.")
        print("0. Voltar")

        try:
            id_evento = int(input("ID do evento: "))

            if id_evento == 0:
                return

            evento = next(
                (evento for evento in eventos if evento.id_ev == id_evento),
                None
            )

            if evento is None:
                print("Evento não encontrado.")
            else:
                try:
                    cliente.inscrever(evento)
                    print("Inscrição realizada com sucesso!")
                except ValueError as erro:
                    print(f"Não foi possível participar: {erro}")

            input("\nPressione ENTER para voltar à lista...")

        except ValueError:
            print("O ID precisa ser um número.")
            input("\nPressione ENTER para voltar à lista...")


def menu_organizador(organizador):
    limpa()

    while True:
        limpa()
        print("=======================")
        print(f"Organizador: {organizador.nome}")
        print("-----------------------")
        print("1. Meus eventos")
        print("2. Criar evento")
        print("3. Sair da conta")
        print("=======================")

        try:
            opcao = int(input("Digite uma opção: "))

            if opcao not in [1, 2, 3]:
                raise ValueError("Número de opção inválido!")

            if opcao == 1:
                menu_meus_eventos(organizador)

            elif opcao == 2:
                criar_evento(organizador)

            elif opcao == 3:
                return

        except ValueError as erro:
            print(f"Erro: {erro}")
            input("\nPressione ENTER para continuar...")


def menu_meus_eventos(organizador):
    limpa()

    while True:
        limpa()
        print("========== MEUS EVENTOS ==========")
        listar_eventos(organizador.eventos)
        print("-----------------------------------")
        print("1. Editar evento")
        print("2. Excluir evento")
        print("0. Voltar")

        try:
            opcao = int(input("Digite uma opção: "))

            if opcao == 0:
                return
            if opcao not in [1, 2]:
                raise ValueError("Número de opção inválido!")

            if not organizador.eventos:
                print("Você ainda não possui eventos para alterar.")
                input("\nPressione ENTER para continuar...")
                continue

            evento = buscar_evento(organizador.eventos)
            if evento is None:
                input("\nPressione ENTER para continuar...")
                continue

            if opcao == 1:
                editar_evento(organizador, evento)
            elif opcao == 2:
                excluir_evento(organizador, evento)

        except ValueError as erro:
            print(f"Erro: {erro}")
            input("\nPressione ENTER para continuar...")


def criar_evento(organizador):
    limpa()

    print("========== CRIAR EVENTO ==========")

    try:
        nome = input("Nome do evento: ")
        data = datetime.strptime(
            input("Data e hora (DD/MM/AAAA HH:MM): "),
            "%d/%m/%Y %H:%M"
        )
        local = input("Local: ")
        idade_minima = int(input("Idade mínima: "))
        valor = float(input("Valor do ingresso: "))
        vagas = int(input("Quantidade de vagas: "))

        organizador.CriarEvento(
            nome, data, local, idade_minima, valor, vagas
        )
        print("Evento criado com sucesso!")

    except ValueError as erro:
        print(f"Não foi possível criar o evento: {erro}")

    input("\nPressione ENTER para continuar...")


def editar_evento(organizador, evento=None):
    if evento is None:
        limpa()
        listar_eventos(organizador.eventos)
        evento = buscar_evento(organizador.eventos)

    if evento is None:
        input("\nPressione ENTER para continuar...")
        return

    limpa()
    
    print(f"========== EDITAR: {evento.nome} ==========")
    print("Deixe em branco os campos que não deseja alterar.")

    try:
        nome = input(f"Nome [{evento.nome}]: ")
        data_texto = input(
            f"Data e hora [{evento.data:%d/%m/%Y %H:%M}]: "
        )
        local = input(f"Local [{evento.local}]: ")
        idade_texto = input(f"Idade mínima [{evento.idade_minima}]: ")
        valor_texto = input(f"Valor [{evento.valor}]: ")
        vagas_texto = input(f"Vagas [{evento.vagas}]: ")

        organizador.EditarEvento(
            evento,
            nome=nome if nome else None,
            data=datetime.strptime(data_texto, "%d/%m/%Y %H:%M")
            if data_texto else None,
            local=local if local else None,
            idade_minima=int(idade_texto) if idade_texto else None,
            valor=float(valor_texto) if valor_texto else None,
            vagas=int(vagas_texto) if vagas_texto else None
        )

        print("Evento atualizado com sucesso!")

    except ValueError as erro:
        print(f"Não foi possível editar o evento: {erro}")

    input("\nPressione ENTER para voltar aos meus eventos...")


def excluir_evento(organizador, evento=None):
    if evento is None:
        limpa()
        listar_eventos(organizador.eventos)
        evento = buscar_evento(organizador.eventos)

    if evento is None:
        input("\nPressione ENTER para continuar...")
        return

    limpa()
    confirmacao = input(
        f"Tem certeza que deseja excluir '{evento.nome}'? (s/n): "
    ).lower()

    if confirmacao == "s":
        try:
            organizador.RemoverEvento(evento)
            print("Evento excluído com sucesso!")
        except ValueError as erro:
            print(f"Não foi possível excluir o evento: {erro}")
    else:
        print("Exclusão cancelada.")

    input("\nPressione ENTER para voltar aos meus eventos...")


# Chama a função do menu principal / inicia o menu
menu_principal()