import itertools
import hashlib

class Pessoa:
    id_obj = itertools.count(1)
    cargo = 0

    def __init__ (self, nome: str, cpf: str, idade: int):
        self.id_user = next(Pessoa.id_obj)
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.cargo = self.cargo
        self.senhaH = None

    def __str__ (self) -> str:
        return (f"ID: {self.id_user} | Nome: {self.nome} | CPF: {self.cpf} | Idade: {self.idade} | Cargo: {self.cargo}")
    
    @classmethod
    def CriarConta(cls, nome: str, cpf: str, idade: int, senha: str):
        if not nome:
            raise ValueError("O nome não pode ser vazio")
        if len(senha) < 6:
            raise ValueError("Senha muito curta")

        pessoa = cls(nome, cpf, idade)
        pessoa.idade = idade
        pessoa.senhaH = cls.gerarHash(senha)
        return pessoa

    def Autenticar (cpf: str, senha: str) -> bool:
        return self.email == email and self.senhaH == self.gerarHash(senha)

    @staticmethod
    def gerarHash(senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()