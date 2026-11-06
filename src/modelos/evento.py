import itertools

class Evento:
    id_obj = itertools.count(1)

    def __init__ (self, local: str, data, valor: float)
        self.id_event = next(Evento.id_obj)
        self. local = local
        self.data = data
        self.valor = valor
