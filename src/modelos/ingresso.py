from itertools import count

class Ingresso:
    id_ing = count(1)

    def __init__(self, cliente, evento):
        self.id = next(Ingresso.id_ing)
        self.cliente = cliente
        self.evento = evento
        self.valor = evento.valor

    def __str__(self): # formatação para texto simples
        return f"Ingresso #{self.id} | {self.evento.nome} ({self.cliente.nome})"

    def __repr__(self): # formatação para lista
        return self.__str__()