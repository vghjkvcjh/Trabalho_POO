# Pacote com as classes do projeto

from .pessoa import Pessoa
from .cliente import Cliente
from .organizador import Organizador
from .ingresso import Ingresso
from .evento import Evento
from .sistema import Sistema

# Define quais classes serão disponibilizadas ao utilizar "from modelos import"
# Isso controla quais nomes fazem parte da interface pública do pacote.

__all__ = [
    "Pessoa",
    "Cliente",
    "Organizador",
    "Ingresso",
    "Evento",
    "Sistema",
]