from .pessoa import Pessoa
from .cliente import Cliente
from .organizador import Organizador
from .ingresso import Ingresso
from .evento import Evento
import hashlib


class Sistema:
    def __init__ (self) -> None:
        self._contas: dict[str, Pessoa] = {}
        self._eventos: dict[str, Evento] = {}

    @staticmethod
    def _gerarHash (senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()

    def Autenticar (self, cpf: str, senha: str) -> bool:
        return self.cpf == cpf and self.senhaH == self.gerarHash(senha)

    def criarConta (self, tipo: type[Pessoa], nome: str, cpf: str, idade: int, senha: str) -> Pessoa:
        if not nome:
            raise ValueError("O nome não pode ser nulo")
        if len(senha) <= 6:
            raise ValueError("A senha não pode ser muito curta")
        if cpf in self._contas:
            raise ValueError("A conta já existe")
        
        pessoa = tipo(nome, cpf, idade)
        pessoa.senhaH = self._gerarHash(senha)
        self._contas[cpf] = pessoa
        return pessoa

    def criarCliente (self, nome: str, cpf: str, idade: int, senha: str) -> Cliente:
        return self.criarConta(Cliente, nome, cpf, idade, senha)

    def criarOrganizador (self, nome: str, cpf: str, idade: int, senha: str) -> Organizador:
        return self.criarConta(Organizador, nome, cpf, idade, senha)

    def Login(self, cpf: str, senha: str):
        pessoa = self._contas.get(cpf) # procura o objeto na lista

        if pessoa is None or not pessoa.senhaH(senha) != self._gerarHash(senha):
            raise ValueError("CPF e/ou Senha incorretos")

        return pessoa