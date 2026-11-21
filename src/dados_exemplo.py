from __future__ import annotations
from datetime import datetime, timedelta
from modelos import Sistema
from modelos.evento import Esportivo, Palestra, Show

SENHA_PADRAO = "123456"

# Função de Data e Hora
def _em(dias: int, hora: int, minuto: int = 0) -> datetime:
    alvo = datetime.now() + timedelta(days=dias)
    return alvo.replace(hour=hora, minute=minuto, second=0, microsecond=0)

# Função de Carregamento
def carregar_dados_exemplo(sistema: Sistema) -> None:

    # Organizadores
    marina = sistema.criarOrganizador("Marina Alves", "52998224725", 41, SENHA_PADRAO)
    rafael = sistema.criarOrganizador("Rafael Torres", "11144477735", 47, SENHA_PADRAO)

    # Clientes
    ana = sistema.criarCliente("Ana Souza", "39053344888", 28, SENHA_PADRAO)
    bruno = sistema.criarCliente("Bruno Lima", "12345678909", 21, SENHA_PADRAO)
    carla = sistema.criarCliente("Carla Mendes", "74821635909", 66, SENHA_PADRAO)
    diego = sistema.criarCliente("Diego Rocha", "28519463746", 14, SENHA_PADRAO)
    lucas = sistema.criarCliente("Lucas Pereira", "46183729582", 10, SENHA_PADRAO)

    # Eventos
    show_rock = marina.CriarEvento(
        Show, "Rock na Praça", _em(45, 21), "Parque da Cidade", 16, 120.0, 5000
    )
    rafael.CriarEvento(
        Show, "Noite Sertaneja", _em(60, 22), "Espaço Vale Hall", 18, 90.0, 2000
    )
    palestra_py = marina.CriarEvento(
        Palestra, "Python para Todos", _em(20, 19), "Auditório Central", 0, 40.0, 150
    )
    oficina = rafael.CriarEvento(
        Palestra, "Oficina de Git (turma reduzida)", _em(15, 14), "Laboratório 3", 0, 30.0, 3
    )
    final = rafael.CriarEvento(
        Esportivo, "Final do Campeonato Regional", _em(30, 16), "Estádio Municipal", 0, 80.0, 30000
    )

    # Inscrições
    ana.inscrever(show_rock)
    bruno.inscrever(show_rock)
    carla.inscrever(show_rock)
    ana.inscrever(palestra_py)
    bruno.inscrever(palestra_py)
    ana.inscrever(oficina)
    bruno.inscrever(oficina)
    ana.inscrever(final)
    lucas.inscrever(final)
    diego.inscrever(final)