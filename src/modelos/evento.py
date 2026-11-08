from datetime import datetime
import itertools

class Evento:
    id_obj = itertools.count(1)

    def __init__ (self, nome, data: datetime, local: str, organizador, valor: float):
        self.id_ev = next(Evento.id_obj)
        self.nome = nome
        self. local = local
        self.data = data
        self.organizador = organizador
        self.valor = valor

    # função utilizada para listar os eventos
    def __str__ (self) -> str:
        return f"Evento({self.nome} | {self.local} | {self.data:%d/%m/%Y %H:%M} | R${self.valor:.2f})"

