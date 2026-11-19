import itertools
from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING

from modelos import Ingresso
from modelos import Cliente
from modelos import Organizador


class Evento(ABC): # Definido como classe abstrata

    _contador_id = itertools.count(1)
    total_criados: int = 0

    # --- construtor ---
    def __init__(self, nome: str, data: datetime, local: str, idade_minima: int,
                 organizador: Organizador, valor_base: float, capacidade: int) -> None:
        self._ingressos: list[Ingresso] = []  # Composição. O evento possuí ingressos
        self.id_ev = next(Evento._contador_id)
        self.nome = nome
        self.data = data
        self.local = local
        self.idade_minima = idade_minima
        self.organizador = organizador
        self.valor_base = valor_base
        self.capacidade = capacidade
        Evento.total_criados += 1

    # Validação do valor base
    @property
    def valor_base(self) -> float:
        # Retorna o valor base antes de regras específicas
        return self._valor_base

    @valor_base.setter # Regras de formatação
    def valor_base(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        self._valor_base = valor

    # Validação da capacidade
    @property
    def capacidade(self) -> int:
        return self._capacidade

    @capacidade.setter # Regras de formatação
    def capacidade(self, valor: int) -> None:
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("A capacidade deve ser um inteiro positivo.")
        if valor < len(self._ingressos):
            raise ValueError("Capacidade menor que a quantidade de ingressos vendidos.")
        self._capacidade = valor

    # Properties simplesmente calculadas
    @property
    def vagas_disponiveis(self) -> int:
        return self._capacidade - len(self._ingressos)

    @property
    def ocupacao(self) -> float:
        """Percentual da capacidade já vendido."""
        return len(self._ingressos) / self._capacidade * 100

    @property
    def faturamento(self) -> float:
        return sum(i.valor for i in self._ingressos)

    @property
    def ingressos(self) -> tuple[Ingresso, ...]:
        """Visão somente leitura dos ingressos vendidos."""
        return tuple(self._ingressos)

    # Exige que todas as subclasses contenham essa funções sem definir como
    @property
    @abstractmethod
    def tipo(self) -> str: ...

    @abstractmethod
    def calcular_preco(self, cliente: Cliente) -> float: ...

    @abstractmethod
    def pode_acessar(self, cliente: Cliente) -> bool: ...

    def vender_ingresso(self, cliente: Cliente) -> Ingresso:
        """Valida as regras e registra a venda."""
        if not self.pode_acessar(cliente):
            raise ValueError("Cliente não atende às regras de acesso do evento.")
        if self.vagas_disponiveis <= 0:
            raise ValueError("Evento sem vagas disponíveis.")
        if any(c.cliente is cliente for c in self._ingressos):
            raise ValueError("Cliente já possui ingresso para este evento.")
        ingresso = Ingresso(cliente, self, self.calcular_preco(cliente))
        self._ingressos.append(ingresso)
        return ingresso

    def cancelar_ingresso(self, ingresso: Ingresso) -> None:
        if ingresso not in self._ingressos:
            raise ValueError("Ingresso não pertence a este evento.")
        self._ingressos.remove(ingresso)

    @classmethod
    def total_de_eventos(cls) -> int:
        return Evento.total_criados

    # Representação em texto
    def exportar(self) -> str:
        """Resumo em uma linha (usado pelo Protocol Exportavel, R10)."""
        return f"[{self.tipo}] {self.nome} | {self.ocupacao:.0f}% ocupado | R${self.faturamento:.2f}"

    def __str__(self) -> str:
        return (f"{self.tipo}: {self.nome} | Local: {self.local} | "
                f"Idade mínima: {self.idade_minima} | Data: {self.data:%d/%m/%Y %H:%M} | "
                f"R${self.valor_base:.2f} | Vagas: {self.vagas_disponiveis}/{self.capacidade}")

# Essas classes possuem suas regras específicas
class Show(Evento):
    # Cobra taxa de serviço e possui idade mínima
    TAXA_SERVICO = 0.10

    @property
    def tipo(self) -> str:
        return "Show"

    def calcular_preco(self, cliente: Cliente) -> float:
        return self.valor_base * (1 + self.TAXA_SERVICO)

    def pode_acessar(self, cliente: Cliente) -> bool:
        return cliente.idade >= self.idade_minima


class Palestra(Evento):
    # Não possui idade mínima e tem desconto para pessoas com menos de 26 anos
    @property
    def tipo(self) -> str:
        return "Palestra"

    def calcular_preco(self, cliente: Cliente) -> float:
        return self.valor_base * 0.5 if cliente.idade <= 25 else self.valor_base

    def pode_acessar(self, cliente: Cliente) -> bool:
        return True


class Esportivo(Evento):
    # Não tem idade mínima e concede meia entrada para pessoas com menos de 12 anos ou mais de 59
    @property
    def tipo(self) -> str:
        return "Esportivo"

    def calcular_preco(self, cliente: Cliente) -> float:
        meia = cliente.idade < 12 or cliente.idade >= 60
        return self.valor_base * 0.5 if meia else self.valor_base

    def pode_acessar(self, cliente: Cliente) -> bool:
        return cliente.idade >= self.idade_minima