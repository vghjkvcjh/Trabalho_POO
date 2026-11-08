from datetime import datetime
from modelos.organizador import Organizador

# org = Organizador("Natan", "123.456.789-00", 20, 1)
# evento = org.CriarEvento("Festa de aniversário", datetime(2026, 12, 20, 19, 0), "Jundiaí", 50)

# org.EditarEvento(evento, local = "São Paulo", valor = 10)

# print(org.eventos)
# print(len(org.eventos))

org = Organizador.CriarConta("Natan", "123.456.789-11", 22, "12345678")
org.CriarEvento("Festa", datetime(2026, 12, 20, 19, 0), "Jundiaí", 50)
org2 = Organizador.CriarConta("Ana", "987.654.321-00", 30, "senha123")
org2.CriarEvento("Show", datetime(2026, 12, 25, 20, 0), "Jundiaí", 80)

Organizador.ListarTodos()