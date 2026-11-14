from modelos.pessoa import Pessoa
from modelos.ingresso import Ingresso

# Base do Cliente
class Cliente(Pessoa):
    cargo = 0
    def __init__ (self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)
        self.ingressosP = [] # Lista de Ingressos que o Cliente possui

    # Função para se inscrever em eventos
    def inscrever(self, evento):
        for ingresso in self.ingressosP: 
            if ingresso.evento is evento:
                raise ValueError("Cliente já possui ingresso para este evento") # Retorna a mensagem em erros de sobreposição de igresso 

        if self.idade < evento.idade_minima:
            raise ValueError("Idade mínima não atingida para este evento") # Retorna a mensagem em erros de idade não atingir o mínimo

        if evento.vagas <= 0:
            raise ValueError("Evento sem vagas disponíveis") # Retorna a mensagem caso não tenha mais vagas disponíveis

        ingresso = Ingresso(self, evento)
        self.ingressosP.append(ingresso)
        evento.vagas -= 1  # Ocupa uma vaga
        return self.ingressosP