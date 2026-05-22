class Churrasco:
    def __init__(self, nome, qtd_pessoas):
        self.nome = nome
        self.qtd_pessoas = qtd_pessoas
#        self.total_qtd_carne = total_qtd_carne
#        self.total_custo_churrasco = total_custo_churrasco
#        self.preco_por_pessoa = preco_por_pessoa

    def apresentar(self):
        self.total_qtd_carne = self.qtd_pessoas * 0.400
        self.total_custo_churrasco = self.total_qtd_carne * 82.4
        self.preco_por_pessoa = self.total_custo_churrasco / self.qtd_pessoas
        return f"Analisando o {self.nome} com {self.qtd_pessoas} convidados. \n Cada participante comerá 0.4kg e cada kg custa R$82,40.\n Recomendo comprar {self.total_qtd_carne}kg de carne.\n O custo total será de R${self.total_custo_churrasco:,.2f}.\n Cada pessoa pagará R${self.preco_por_pessoa:,.2f} para participar." 

# Cada pessoa pagará R$32.96 para participar. 

c1 = Churrasco("Churras dos Amigos", 15)
print(c1.apresentar())

#Considere:
#Consumo padrão: 400gr por pessoa
#Preço: R$82,40

# imprime etiqueta
# Analisando Churras dos amigos com 15 convidades
# Cada participante comerá 0.4kg e cada kg custa R$82.40
# Recomento comprar 6.000kg de carne
# O custo total será de R$494.40
# Cada pessoa pagará R$32.96 para participar.