from modelos.pessoa import Pessoa
from modelos.ingresso import Ingresso

# base do cliente
class Cliente(Pessoa):
    cargo = 0
    def __init__ (self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)
        self.ingressosP = []

    def inscrever(self, evento):
        for ingresso in self.ingressosP:
            if ingresso.evento is evento:
                raise ValueError("Cliente já possui ingresso para este evento")

        if self.idade < evento.idade_minima:
            raise ValueError("Idade mínima não atingida para este evento")

        if evento.vagas <= 0:
            raise ValueError("Evento sem vagas disponíveis")

        ingresso = Ingresso(self, evento)
        self.ingressosP.append(ingresso)
        evento.vagas -= 1  # ocupa uma vaga
        return self.ingressosP