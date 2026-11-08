import itertools
from datetime import datetime

class Evento:
    id_obj = itertools.count(1)

    def __init__ (self, nome, data: datetime, local: str, organizador, valor: float):
        self.nome = nome
        self. local = local
        self.data = data
        self.organizador = organizador
        self.valor = valor

    def __repr__ (self):
        return f"Evento({self.nome}, {self.local}, {self.data:%d/%m/%Y %H:%M}, R$ {self.valor:.2f})"
