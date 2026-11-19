from .pessoa import Pessoa
from .evento import Evento
from datetime import datetime

class Organizador(Pessoa):

    def __init__(self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)
        self.eventos: list[Evento] = []

    def CriarEvento(self, tipo: type[Evento], nome: str, data: datetime, local: str, idade_minima: int, valor: float, capacidade: int) -> Evento:
        if not isinstance(tipo, type) or not issubclass(tipo, Evento):
            raise TypeError("O tipo deve ser uma subclasse de Evento.")
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        evento = tipo(nome.strip(), data, local, idade_minima, self, valor, capacidade)
        self.eventos.append(evento)
        return evento

    def EditarEvento(self, evento: Evento, nome: str | None = None, data: datetime | None = None, local: str | None = None, idade_minima: int | None = None, valor: float | None = None, capacidade: int | None = None) -> None:
        # Substitui apenas as informações dadas, pulando as nulas
        if evento not in self.eventos:
            raise ValueError("Este evento não pertence a este organizador.")
        if nome is not None:
            evento.nome = nome
        if data is not None:
            evento.data = data
        if local is not None:
            evento.local = local
        if idade_minima is not None:
            evento.idade_minima = idade_minima
        if valor is not None:
            evento.valor_base = valor
        if capacidade is not None:
            evento.capacidade = capacidade

    def RemoverEvento(self, evento: Evento) -> None:
        if evento not in self.eventos:
            raise ValueError("Este evento não pertence a este organizador.")
        if evento.ingressos:
            raise ValueError("Não é possível excluir um evento que já possui ingressos vendidos.")
        self.eventos.remove(evento)

    def __str__(self) -> str:
        return f"{super().__str__()} | Eventos: {len(self.eventos)}"
