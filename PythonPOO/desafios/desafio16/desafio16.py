from rich import print
from rich import inspect 

class Funcionario:

    # Atributo de Classe
    empresa = "Curso em vídeo"


    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake:Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}."

# Funcionario.empresa = "Globo"

c1 = Funcionario("Willian", "Administração", "Supervisor")

print(c1.__dict__)
# inspect(c1, methods=True)
print(c1.apresentacao())
# inspect(c1, all=True)