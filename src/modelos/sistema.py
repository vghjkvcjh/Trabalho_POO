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
    def _gerarHash(senha: str) -> str:
        if not isinstance(senha, str):
            raise TypeError("A senha deve ser texto.")
        return hashlib.sha256(senha.encode("utf-8")).hexdigest()

    def Autenticar(self, cpf: str, senha: str) -> bool:
        pessoa = self._contas.get(cpf)
        if pessoa is None or pessoa.senhaH is None:
            return False
        return pessoa.senhaH == self._gerarHash(senha)

    def criarConta(self, tipo: type[Pessoa], nome: str, cpf: str, idade: int, senha: str) -> Pessoa:
        if not isinstance(tipo, type) or not issubclass(tipo, Pessoa):
            raise TypeError("O tipo de conta deve ser Cliente ou Organizador.")
        if not isinstance(senha, str) or len(senha) < 6:
            raise ValueError("A senha deve ter no mínimo 6 caracteres.")
        if cpf in self._contas:
            raise ValueError("Já existe uma conta cadastrada com este CPF.")
        pessoa = tipo(nome, cpf, idade)
        pessoa.senhaH = self._gerarHash(senha)
        self._contas[cpf] = pessoa
        return pessoa

    def criarCliente(self, nome: str, cpf: str, idade: int, senha: str) -> Cliente:
        return self.criarConta(Cliente, nome, cpf, idade, senha)

    def criarOrganizador(self, nome: str, cpf: str, idade: int, senha: str) -> Organizador:
        return self.criarConta(Organizador, nome, cpf, idade, senha)

    def Login(self, cpf: str, senha: str) -> Pessoa:
        if not self.Autenticar(cpf, senha):
            raise ValueError("CPF e/ou senha incorretos.")
        return self._contas[cpf]

    def ListarEventos(self) -> list[Evento]:
        eventos: list[Evento] = []
        for pessoa in self._contas.values():
            if isinstance(pessoa, Organizador):
                eventos.extend(pessoa.eventos)
        return eventos

    def ListarOrganizadores(self) -> None:
        organizadores = [pessoa for pessoa in self._contas.values() if isinstance(pessoa, Organizador)]
        if not organizadores:
            print("Nenhum organizador registrado.")
            return
        for organizador in organizadores:
            print(organizador)
            for evento in organizador.eventos:
                print(f"    -> {evento}")
