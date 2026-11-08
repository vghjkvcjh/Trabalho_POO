from datetime import datetime
import itertools

class Evento:
    id_obj = itertools.count(0)
    def __init__ (self, nome, data: datetime, local: str, organizador, valor: float):
        self.id_ev = next(Evento.id_obj)
        self.nome = nome
        self. local = local
        self.data = data
        self.organizador = organizador
        self.valor = valor

    def __repr__ (self):
        return f"Evento({self.nome}, {self.local}, {self.data:%d/%m/%Y %H:%M}, R$ {self.valor:.2f})"
