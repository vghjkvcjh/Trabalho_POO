from __future__ import annotations

import itertools
import math
from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING

from .ingresso import Ingresso

if TYPE_CHECKING:
    from .cliente import Cliente
    from .organizador import Organizador


class Evento(ABC):
    # Evento com controle de capacidade, acesso e venda de ingressos.

    _contador_id = itertools.count(1)
    total_criados: int = 0

    def __init__(self, nome: str, data: datetime, local: str, idade_minima: int, organizador: Organizador, valor_base: float, capacidade: int) -> None:
        self._ingressos: list[Ingresso] = []
        self.id_ev = next(Evento._contador_id)
        self.nome = nome
        self.data = data
        self.local = local
        self.idade_minima = idade_minima
        self.organizador = organizador
        self.valor_base = valor_base
        self.capacidade = capacidade
        Evento.total_criados += 1

    @staticmethod
    def _validar_texto(valor: str, campo: str) -> str:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"{campo} não pode ser vazio.")
        return valor.strip()

    @staticmethod
    def _validar_idade(valor: int) -> int:
        if isinstance(valor, bool) or not isinstance(valor, int) or valor < 0:
            raise ValueError("A idade mínima deve ser um inteiro não negativo.")
        return valor

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str) -> None:
        self._nome = self._validar_texto(valor, "O nome")

    @property
    def data(self) -> datetime:
        return self._data

    @data.setter
    def data(self, valor: datetime) -> None:
        if not isinstance(valor, datetime):
            raise TypeError("A data do evento deve ser um datetime.")
        self._data = valor

    @property
    def local(self) -> str:
        return self._local

    @local.setter
    def local(self, valor: str) -> None:
        self._local = self._validar_texto(valor, "O local")

    @property
    def idade_minima(self) -> int:
        return self._idade_minima

    @idade_minima.setter
    def idade_minima(self, valor: int) -> None:
        self._idade_minima = self._validar_idade(valor)

    @property
    def valor_base(self) -> float:
        return self._valor_base

    @valor_base.setter
    def valor_base(self, valor: float) -> None:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("O valor deve ser numérico.")
        if not math.isfinite(valor) or valor < 0:
            raise ValueError("O valor deve ser finito e não negativo.")
        self._valor_base = float(valor)

    @property
    def capacidade(self) -> int:
        return self._capacidade

    @capacidade.setter
    def capacidade(self, valor: int) -> None:
        if isinstance(valor, bool) or not isinstance(valor, int) or valor <= 0:
            raise ValueError("A capacidade deve ser um inteiro positivo.")
        if valor < len(self._ingressos):
            raise ValueError("Capacidade menor que a quantidade de ingressos vendidos.")
        self._capacidade = valor

    @property
    def vagas_disponiveis(self) -> int:
        return self._capacidade - len(self._ingressos)

    @property
    def ocupacao(self) -> float:
        return len(self._ingressos) / self._capacidade * 100

    @property
    def faturamento(self) -> float:
        return sum(ingresso.valor for ingresso in self._ingressos)

    @property
    def ingressos(self) -> tuple[Ingresso, ...]:
        return tuple(self._ingressos)

    @property
    @abstractmethod
    def tipo(self) -> str:
        ...

    @abstractmethod
    def calcular_preco(self, cliente: Cliente) -> float:
        ...

    @abstractmethod
    def pode_acessar(self, cliente: Cliente) -> bool:
        ...

    def vender_ingresso(self, cliente: Cliente) -> Ingresso:
        if not self.pode_acessar(cliente):
            raise ValueError("Cliente não atende às regras de acesso do evento.")
        if self.vagas_disponiveis <= 0:
            raise ValueError("Evento sem vagas disponíveis.")
        if any(ingresso.cliente is cliente for ingresso in self._ingressos):
            raise ValueError("Cliente já possui ingresso para este evento.")
        ingresso = Ingresso(cliente, self, self.calcular_preco(cliente))
        self._ingressos.append(ingresso)
        return ingresso

    def cancelar_ingresso(self, ingresso: Ingresso) -> None:
        if ingresso not in self._ingressos:
            raise ValueError("Ingresso não pertence a este evento.")
        self._ingressos.remove(ingresso)
        if ingresso in ingresso.cliente._ingressos:
            ingresso.cliente._ingressos.remove(ingresso)

    @classmethod
    def total_de_eventos(cls) -> int:
        return Evento.total_criados

    def __str__(self) -> str:
        return (
            f"{self.tipo}: {self.nome} | Local: {self.local} | "
            f"Idade mínima: {self.idade_minima} | Data: {self.data:%d/%m/%Y %H:%M} | "
            f"Valor base: R${self.valor_base:.2f} | "
            f"Vagas: {self.vagas_disponiveis}/{self.capacidade}"
        )

class Show(Evento):
    #Show cobra taxa de serviço e respeita a idade mínima.

    TAXA_SERVICO = 0.10

    @property
    def tipo(self) -> str:
        return "Show"

    @property
    def preco_com_taxa(self) -> float:
        return round(self.valor_base * (1 + self.TAXA_SERVICO), 2)

    def calcular_preco(self, cliente: Cliente) -> float:
        return self.preco_com_taxa

    def exportar(self) -> str:
        return (
            f"[{self.tipo}] {self.nome} | Valor base: R${self.valor_base:.2f} | "
            f"Preço com taxa: R${self.preco_com_taxa:.2f} | "
            f"{self.ocupacao:.0f}% ocupado | Faturamento: R${self.faturamento:.2f}"
        )

    def pode_acessar(self, cliente: Cliente) -> bool:
        return cliente.idade >= self.idade_minima


class Palestra(Evento):
    # Palestra oferece meia-entrada a participantes de até 25 anos.

    @property
    def tipo(self) -> str:
        return "Palestra"

    def calcular_preco(self, cliente: Cliente) -> float:
        return round(self.valor_base * 0.5, 2) if cliente.idade <= 25 else self.valor_base

    def pode_acessar(self, cliente: Cliente) -> bool:
        return True


class Esportivo(Evento):
    # Evento esportivo oferece meia-entrada a menores de 12 e maiores de 59.

    @property
    def tipo(self) -> str:
        return "Esportivo"

    def calcular_preco(self, cliente: Cliente) -> float:
        meia = cliente.idade < 12 or cliente.idade >= 60
        return round(self.valor_base * 0.5, 2) if meia else self.valor_base

    def pode_acessar(self, cliente: Cliente) -> bool:
        return cliente.idade >= self.idade_minima
