from __future__ import annotations 
import os
import sys 

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # pega a pasta deste arquivo e a coloca no início da lista de importação

from dados_exemplo import carregar_dados_exemplo
from menu import menu_principal
from modelos import Sistema

def main() -> None: # Cria o Sistema, Carrega os Dados de Exemplo e Executa o Menu
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # Força a Saída do Terminal a Usar UTF-8
    except (AttributeError, ValueError):
        pass
    sistema = Sistema()  # Cria Uma Instância do Sistema Vazio
    carregar_dados_exemplo(sistema)
    menu_principal(sistema) # Abre o Menu Com o Sistema


if __name__ == "__main__":
    main()