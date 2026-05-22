class Churrasco:
    def __init__(self, qtd_pessoas, total_qtd_carne, total_custo_churrasco,preco_por_pessoa):
        self.qtd_pessoas = qtd_pessoas
        self.total_qtd_carne = total_qtd_carne
        self.total_custo_churrasco = total_custo_churrasco
        self.preco_por_pessoa = preco_por_pessoa

    def apresentacao(self):
        return f"{self.nome} é o novo funcionário do setor de {self.setor} e entra no cargo de {self.cargo}."

c1 = Funcionario("Willian", "Argamassa", "Supervisor")

print(c1.apresentacao())

#Classe Churrasco 

#quantas pessoas
#quanto de carne
#custo total
#preço por pessoa

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()

#Considere:
#Consumo padrão: 400gr por pessoa
#Preço: R$82,40

# imprime etiqueta
# Analisando Churras dos amigos com 15 convidades
# Cada participante comerá 0.4kg e cada kg custa R$82.40
# Recomento comprar 6.000kg de carne
# O custo total será de R$494.40
# Cada pessoa pagará R$32.96 para participar.