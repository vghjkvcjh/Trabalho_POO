from .pessoa import Pessoa
from .evento import Evento
from datetime import datetime

class Organizador(Pessoa):

    def __init__ (self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)
        self.eventos = []
    
    def CriarEvento(self, tipo: type[Evento], nome: str, data: datetime, local: str, idade_minima: int, valor: float, capacidade: int) -> Evento:
        # Cria um evento do tipo informado (Show, Palestra ou Esportivo)
        if not nome:
            raise ValueError("O nome não pode ser vazio")
        if not (isinstance(tipo, type) and issubclass(tipo, Evento)):
            raise TypeError("O tipo deve ser uma subclasse de Evento.")

        evento = tipo(nome, data, local, idade_minima, self, valor, capacidade)

        self.eventos.append(evento)
        return evento

    def EditarEvento(self, evento: Evento, nome: str | None = None, data: datetime | None = None, local: str | None = None, idade_minima: int | None = None, valor: float | None = None, capacidade: int | None = None) -> None:
        # Altera apenas os campos informados; os demais permanecem como estão.
        if evento not in self.eventos:
            raise ValueError("Este evento não te pertence")

        if nome is not None:
            if not nome:
                raise ValueError("O nome não pode ser vazio")
            evento.nome = nome
        if data is not None:
            evento.data = data
        if local is not None:
            evento.local = local
        if idade_minima is not None:
            evento.idade_minima = idade_minima
        if valor is not None:
            evento.valor_base = valor        # passa pelo setter e valida
        if capacidade is not None:
            evento.capacidade = capacidade   # passa pelo setter e valida

    # função utilizada para listar os organizadores + eventos que a eles pertecem
    def __str__ (self) -> str:
        base = super().__str__()
        return f"{base} | Eventos: {len(self.eventos)}"