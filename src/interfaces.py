from typing import Protocol, runtime_checkable

@runtime_checkable
class Exportavel(Protocol): # Força uma classe que seja Exportavel a ter a função exportar
    def exportar(self) -> str: ...