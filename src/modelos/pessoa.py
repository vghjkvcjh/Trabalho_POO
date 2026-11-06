import itertools

class Pessoa:
    id_obj = itertools.count(1)

    def __init__ (self, nome: str, cpf: str)
        self.id_user = next(Pessoa.id_obj)
        self.nome = nome
        self cpf = cpf