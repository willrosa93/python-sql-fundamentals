from abc import ABC, abstractmethod
from datetime import datetime


class ContaBancaria(ABC):

    def __init__(
        self,
        titular,
        saldo=0,
        data_ultimo_deposito=None,
        data_ultimo_rendimento=None
    ):
        self.id = None
        self.titular = titular
        self.saldo = float(saldo)

        self.data_ultimo_deposito = data_ultimo_deposito
        self.data_ultimo_rendimento = data_ultimo_rendimento

    def depositar(self, valor):

        if valor <= 0:
            print("Valor inválido.")
            return

        self.saldo += valor
        self.data_ultimo_deposito = datetime.now()

        print(
            f"Depósito de R${valor:,.2f} realizado com sucesso."
        )

    def sacar(self, valor):

        if valor <= 0:
            print("Valor inválido.")
            return

        if valor > self.saldo:
            print("Saldo insuficiente.")
            return

        self.saldo -= valor

        print(
            f"Saque de R${valor:,.2f} realizado com sucesso."
        )

    @abstractmethod
    def render(self):
        pass

    def __str__(self):

        return (
            f"ID: {self.id} | "
            f"Titular: {self.titular} | "
            f"Saldo: R${self.saldo:,.2f}"
        )


class Conta_Corrente(ContaBancaria):

    def render(self):

        print(
            "Conta corrente não possui rendimento."
        )


class Conta_Poupanca(ContaBancaria):

    TAXA_RENDIMENTO = 0.005

    def pode_render(self):

        if self.data_ultimo_deposito is None:
            return False

        dias = (
            datetime.now() -
            self.data_ultimo_deposito
        ).days

        return dias >= 30

    def render(self):

        if not self.pode_render():

            print(
                "Ainda não passaram 30 dias "
                "desde o último depósito."
            )

            return

        rendimento = (
            self.saldo *
            self.TAXA_RENDIMENTO
        )

        self.saldo += rendimento

        self.data_ultimo_rendimento = datetime.now()

        print(
            f"Rendimento aplicado: "
            f"R${rendimento:,.2f}"
        )