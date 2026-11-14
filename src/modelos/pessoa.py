# importa bibliotecas, uma para criar o id como autoincrement e a outra para codificar senhas
import itertools
from abc import ABC, abstractmethod

class Pessoa:
    id_user = itertools.count(1)
    # a variável cargo será usada posteriormente como redundância para evitar que clientes acessem informações indevidas 
    cargo = 0
    # lista contendo todas as contas criadas
    contas = {}

    @abstractmethod
    def __init__ (self, nome: str, cpf: str, idade: int):
        self.id_user = next(Pessoa.id_user)
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.cargo = self.cargo
        self.senhaH = None

    # função utilizada para listar as contas
    def __str__ (self) -> str:
        return (f"ID: {self.id_user} | Nome: {self.nome} | CPF: {self.cpf} | Idade: {self.idade} | Cargo: {self.cargo}")
    

    @classmethod
    def Login(cls, cpf: str, senha: str):
        pessoa = Pessoa.contas.get(cpf) # procura o objeto na lista

        if pessoa is None or not pessoa.Autenticar(senha):
            raise ValueError("CPF e/ou Senha incorretos")

        return pessoa

    # serve para autentificar uma tentativa de login
    def Autenticar (self, cpf: str, senha: str) -> bool:
        return self.cpf == cpf and self.senhaH == self.gerarHash(senha)