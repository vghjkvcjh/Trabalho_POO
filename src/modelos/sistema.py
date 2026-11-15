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
    def _gerarHash (senha: str) -> str: # gera o hash para a senha do usuário
        return hashlib.sha256(senha.encode()).hexdigest()

    def Autenticar (self, cpf: str, senha: str) -> bool: # compara os valores inseridos com o que o sistema possui
        return self.cpf == cpf and self.senhaH == self.gerarHash(senha)

    def criarConta (self, tipo: type[Pessoa], nome: str, cpf: str, idade: int, senha: str) -> Pessoa: # base para a criação de conta. NÃO USAR
        if not nome: # tratamento de erros
            raise ValueError("O nome não pode ser nulo")
        if len(senha) <= 6:
            raise ValueError("A senha não pode ser muito curta")
        if cpf in self._contas:
            raise ValueError("A conta já existe")
        
        pessoa = tipo(nome, cpf, idade)
        pessoa.senhaH = self._gerarHash(senha)
        self._contas[cpf] = pessoa # adiciona a conta ao dicionário
        return pessoa

    def criarCliente (self, nome: str, cpf: str, idade: int, senha: str) -> Cliente: # função de criar conta para cliente
        return self.criarConta(Cliente, nome, cpf, idade, senha)

    def criarOrganizador (self, nome: str, cpf: str, idade: int, senha: str) -> Organizador: # função de criar conta para organizador
        return self.criarConta(Organizador, nome, cpf, idade, senha)

    def Login(self, cpf: str, senha: str):
        pessoa = self._contas.get(cpf)

        if pessoa is None or not pessoa.senhaH(senha) != self._gerarHash(senha): # compara o hash registrado ao inserido, mostrando erro se não forem iguais
            raise ValueError("CPF e/ou Senha incorretos")

        return pessoa

    def ListarOrganizadores(self) -> None:
        organizadores = [o for o in self._contas.values() if isinstance(o, Organizador)] # percorre todas as contas selecionando apenas aqueles com tipo Organizador

        if not organizadores:
            print("Nenhum organizador registrado")
        
        for org in organizadores: # cria uma variável que recebe informações da lista, mostrando cada um dos organizadores e seus respectivos eventos na tela
            print(org)
            for evento in org.eventos:
                print(f"    -> {evento}")