from datetime import datetime
from modelos.organizador import Organizador

org = Organizador("Natan", "123.456.789-00")
evento = org.CriarEvento("Festa de aniversário", datetime(2026, 12, 20, 19, 0), "Jundiaí", 50)

org.EditarEvento(evento, local = "São Paulo", valor = 10)

print(org.eventos)
print(len(org.eventos))

