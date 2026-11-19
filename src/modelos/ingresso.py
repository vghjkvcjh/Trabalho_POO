from itertools import count

class Ingresso:
    id_ing = count(1)

    def __init__(self, cliente, evento, valor):
        self.id = next(Ingresso.id_ing)
        self.cliente = cliente
        self.evento = evento
        self.valor = valor

    def exportar(self) -> str:
        return (
            f"Ingresso #{self.id} | {self.evento.nome} | "
            f"{self.cliente.nome} | R${self.valor:.2f}"
        )