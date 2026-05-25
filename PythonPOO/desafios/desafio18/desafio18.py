from rich import print 
from rich.panel import Panel 

class Churrasco:
    consumo_padrao:float = 0.400 # Cada participante comerá 0.4kg
    preco_kg:float = 82.40 # Cada Kg de carne custa R$82.40

    def __init__(self, titulo, quant):
        # Atributos de instância
        self.titulo = titulo
        self.participantes = quant
#        self.total_qtd_carne = total_qtd_carne
#        self.total_custo_churrasco = total_custo_churrasco
#        self.preco_por_pessoa = preco_por_pessoa

    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.preco_kg # ou self.__class__.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando o [green]{self.titulo}[/] com [blue]{self.participantes} convidados[/]."
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada kg custa R${Churrasco.preco_kg:,.2f}"
        conteudo += f"\nRecomendo comprar {self.calcular_qtd_carne():,.3f}kg de carne"
        conteudo += f"\nO custo total será de R${self.calcular_custo_total():,.2f}"
        conteudo += f"\nCada pessoa pagará R${self.calcular_custo_individual():,.2f} para participar"
        painel = Panel(conteudo, title=self.titulo)
        print(painel)
#        self.total_qtd_carne = self.quant * 0.400
#        self.total_custo_churrasco = self.total_qtd_carne * 82.4
#        self.preco_por_pessoa = self.total_custo_churrasco / self.quant
#        return f"Analisando o {self.titulo} com {self.participantes} convidados. \n\nRecomendo comprar {self.total_qtd_carne}kg de carne.\nO custo total será de R${self.total_custo_churrasco:,.2f}.\nCada pessoa pagará R${self.preco_por_pessoa:,.2f} para participar." 

# Cada pessoa pagará R$32.96 para participar. 

c1 = Churrasco("Churras dos Amigos", 15)
print(c1.analisar())

#Considere:
#Consumo padrão: 400gr por pessoa
#Preço: R$82,40

# imprime etiqueta
# Analisando Churras dos amigos com 15 convidades
# Cada participante comerá 0.4kg e cada kg custa R$82.40
# Recomento comprar 6.000kg de carne
# O custo total será de R$494.40
# Cada pessoa pagará R$32.96 para participar.