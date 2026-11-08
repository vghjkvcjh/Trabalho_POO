from modelos.pessoa import Pessoa
from modelos.evento import Evento
from datetime import datetime

class Organizador(Pessoa):
    def __init__ (self, nome: str, cpf: str,):
        super().__init__(nome, cpf)
        self.eventos = []
    
    def CriarEvento (self, nome: str, data: datetime, local: str, valor: float) -> Evento:
        if not nome:
            raise ValueError("O nome não pode ser vazio")
        
        evento = Evento (nome=nome, data=data, local=local, organizador=self, valor=valor)

        self.eventos.append(evento)
        return evento

    def EditarEvento (self, evento:Evento, nome: str = None, data: datetime = None, local: str = None, valor: float = None) -> Evento:
        if evento not in self.eventos:
            raise ValueError("Este evento não te pertence")

        if nome is not None:
            evento.nome = nome
        if data is not None:
            evento.data = data
        if local is not None:
            evento.local = local
        if valor is not None:
            evento.valor = valor