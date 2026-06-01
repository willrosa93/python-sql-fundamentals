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

from rich import inspect
from funcionarios import * 

def main():
    f1 = FuncionarioHorista("Paulo", 12, 200)
    f1.calcular_salario()
    f1.analisar_salario()

    f2 = FuncionarioMensalista("Amanda", 9500)
    f2.calcular_salario()
    f2.analisar_salario()

if __name__ == "__main__":
    main()

# Resultado em etiqueta
# Análise de Salário
# O salário de Paulo (FuncionarioHorista) é de
# R$2220.00 e corresponde a 1.4 salários mínimos.

# Análise de Salário
# O salário de Amanda (FuncionarioMensalista) é de
# R$8787.50 e corresponde a 5.5 salários mínimos.