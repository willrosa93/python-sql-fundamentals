from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionarios(ABC):
    sal_min = 1612
    inss = 7.5

    def __init__(self, nome, sal_bruto=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        qtd_salarios = self.salario / self.sal_min

        print("Análise de Salário")
        print(
            f"O salário de {self.nome} "
            f"({type(self).__name__}) é de"
        )
        print(
            f"R${self.salario:.2f} "
            f"e corresponde a {qtd_salarios:.1f} salários mínimos."
        )

class FuncionarioHorista(Funcionarios):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calcular_salario(self):
        self.sal_bruto = self.valor_hora * self.horas_trab

        desconto = self.sal_bruto * (self.inss / 100)

        self.salario = self.sal_bruto - desconto

class FuncionarioMensalista(Funcionarios):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)

    def calcular_salario(self):
        desconto = self.sal_bruto * (self.inss / 100)

        self.salario = self.sal_bruto - desconto

# Crie a estrutura capaz de calcular salários de funcionários diferentes

# Funcionario(abstract)
# nome
# sal_bruto
# salario
# sal_min = 16121
# inss = 7.5
# calc_sal() (abstract)
# analisar_sal()

# Horista
# valor_hora
# horas_trab
# calc_sal()

# Mensalista
# calc_sal

# Resultado em etiqueta
# Análise de Salário
# O salário de Paulo (FuncionarioHorista) é de
# R$2220.00 e corresponde a 1.4 salários mínimos.

# Análise de Salário
# O salário de Amanda (FuncionarioMensalista) é de
# R$8787.50 e corresponde a 5.5 salários mínimos.