from modelos.pessoa import Pessoa
from modelos.evento import Evento
from datetime import datetime

class Organizador(Pessoa):
    cargo = 1
    todos = [] # lista de todos os organizadores

    def __init__ (self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)
        self.eventos = []
        Organizador.todos.append(self) # adiciona o organizador à lista assim que ele é criado
    
    def CriarEvento (self, nome: str, data: datetime, local: str, valor: float) -> Evento:
        if not nome:
            raise ValueError("O nome não pode ser vazio")
        
        evento = Evento (nome=nome, data=data, local=local, organizador=self, valor=valor) # cria uma lista particular que contém todos os eventos criados por um organizador

        self.eventos.append(evento) # adiciona o evento recém criado à lista pessoal de eventos criados
        return evento

    def EditarEvento (self, evento:Evento, nome: str = None, data: datetime = None, local: str = None, valor: float = None) -> Evento:
        if evento not in self.eventos:
            raise ValueError("Este evento não te pertence")

        if nome is not None:
            evento.nome = nome
        if data is not None:
            evento.data = data
        if local is not None:
            evento.local = local
        if valor is not None:
            evento.valor = valor

    # função utilizada para listar os organizadores + eventos que a eles pertecem
    def __str__ (self) -> str:
        base = super().__str__()
        return f"{base} | Eventos: {len(self.eventos)}"

    @classmethod
    def ListarTodos(cls) -> None:
        if not cls.todos:
            print("Nenhum organizador cadastrado.")
            return

        for org in cls.todos:
            print(org)
            for evento in org.eventos:
                print(f"    -> {evento}")