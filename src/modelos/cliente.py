from modelos.pessoa import Pessoa

# base do cliente
class Cliente(Pessoa):
    cargo = 0
    def __init__ (self, nome: str, cpf: str,):
        super().__init__(nome, cpf)

    def inscrever ()