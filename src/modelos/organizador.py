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
        return self.eventos

