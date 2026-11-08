from typing import Protocol

class Exibivel(Protocol):
    """Qualquer objeto que sabe se descrever como texto."""

    def exibir(self) -> str:
        ...

class GerenciadorDeEventos(Protocol):
    """Quem pode criar e editar eventos (ex.: Organizador)."""

    def CriarEvento(self, nome, data, local, valor):
        ...

    def EditarEvento(self, evento, nome=None, data=None, local=None, valor=None):
        ...