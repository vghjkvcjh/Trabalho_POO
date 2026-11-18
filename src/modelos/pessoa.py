# importa bibliotecas, uma para criar o id como autoincrement e a outra para codificar senhas

import itertools
from abc import ABC, abstractmethod

class Pessoa(ABC):
    id_user = itertools.count(1)

    @abstractmethod
    def __init__(self, nome: str, cpf: str, idade: int):
        self.id = next(Pessoa.id_user)
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.senhaH = None

    # Propriedade responsável pela validação do CPF
    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("O CPF deve ser informado como string.")

        if not valor.isdigit():
            raise ValueError("O CPF deve conter apenas números.")

        if len(valor) != 11:
            raise ValueError("O CPF deve conter exatamente 11 dígitos.")

        self._cpf = valor

    @property
    def senhaH(self) -> str:
        return self._senhaH

    @senhaH.setter
    def senhaH(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("A senha deve ser informada como string.")

        if len(valor) < 6:
            raise ValueError("A senha deve ter no mínimo 6 dígitos")
        
        self._senhaH = valor

    
    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("O nome deve ser uma string.")

        if not valor:
            raise ValueError("O nome não pode estar vazio.")

        if not valor[0].isalpha() or not valor[0].isupper():
            raise ValueError("O primeiro caractere do nome deve ser uma letra maiúscula.")

        self._nome = valor


    def __str__(self) -> str:
        return (f"ID: {self.id} | Nome: {self.nome} | CPF: {self.cpf} | Idade: {self.idade} | Cargo: {self.cargo}")
