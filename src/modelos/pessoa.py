# importa bibliotecas, uma para criar o id como autoincrement e a outra para codificar senhas
import itertools
from abc import ABC, abstractmethod

class Pessoa(ABC):
    id_user = itertools.count(1)

    @abstractmethod
    def __init__ (self, nome: str, cpf: str, idade: int):
        self.id = next(Pessoa.id_user)
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.senhaH = None

    # função utilizada para listar as contas
    def __str__ (self) -> str:
        return (f"ID: {self.id} | Nome: {self.nome} | CPF: {self.cpf} | Idade: {self.idade} | Cargo: {self.cargo}")