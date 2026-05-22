class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"{self.nome} é o novo funcionário do setor de {self.setor} e entra no cargo de {self.cargo}."

c1 = Funcionario("Willian", "Argamassa", "Supervisor")

print(c1.apresentacao())