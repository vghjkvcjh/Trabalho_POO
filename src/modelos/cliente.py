from modelos.pessoa import Pessoa
from modelos.ingresso import Ingresso

# Base do Cliente
class Cliente(Pessoa):
    def __init__ (self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)
        self.ingressosP = [] # Lista de Ingressos que o Cliente possui

    # Função para se inscrever em eventos
    def inscrever(self, evento) -> Ingresso:
        ingresso = evento.vender_ingresso(self)   # Regras ficam no Evento
        self._ingressos.append(ingresso)
        return ingresso