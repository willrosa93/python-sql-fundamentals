class ContaBancaria:
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def sacar(self, valor):
        try:
            if valor <= 0:
                raise ValueError("Valor deve ser positivo")
            if valor > self.saldo:
                raise ValueError("Saldo insuficiente")
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")

        except ValueError as e:
            print(f"Erro no saque: {e}")

c1 = ContaBancaria(112, "Willian", 3000)
c1.sacar(20000)
print(c1)