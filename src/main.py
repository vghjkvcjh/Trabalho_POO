# org = Organizador("Natan", "123.456.789-00", 20, 1)
# evento = org.CriarEvento("Festa de aniversário", datetime(2026, 12, 20, 19, 0), "Jundiaí", 50)

# org.EditarEvento(evento, local = "São Paulo", valor = 10)

# print(org.eventos)
# print(len(org.eventos))

# org = Organizador.CriarConta("Natan", "123.456.789-11", 22, "12345678")
# evento = org.CriarEvento("Festa", datetime(2026, 12, 20, 19, 0), "Jundiaí", 10, 50, 20)
# cli1 = Cliente.CriarConta("Ana", "987.654.321-00", 30, "senha123")
# org2.CriarEvento("Show", datetime(2026, 12, 25, 20, 0), "Jundiaí", 80)

# Organizador.ListarTodos()

# ingresso = cli1.inscrever(evento)
# print(ingresso)

from __future__ import annotations

import os
import sys

# Permite rodar de qualquer pasta: coloca "src/" no caminho de importação.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from menu import Menu
from modelos import Sistema

# Cria o Sistema, Carrega os dados de exemplo e abre o menu interativo.
def main() -> None:
    try: sys.stdout.reconfigure(encoding="utf-8") # Garante acentos corretos em terminais que não usam UTF-8 por padrão
    except (AttributeError, ValueError): pass
    sistema = Sistema()
    carregar_dados_exemplo(sistema)
    print("Dados de exemplo carregados (organizadores, participantes, eventos e vendas).")
    Menu(sistema).executar()

if __name__ == "__main__":
    main()