# Definindo a função
def saudacao():
    print("Olá! Bem-vindo ao Python!")
# Chamando a função
saudacao()
saudacao() # pode chamar quantas vezes quiser
saudacao() # pode chamar quantas vezes quiser

# Parâmetros são as "entradas" da função
def somar(a, b):
    resultado = a + b
    return resultado # return devolve o valor

total = somar(5, 3)
print(f"5 + 3 = {total}") # 5 + 3 = 8

# Parâmetros com valor padrão
def apresentar(nome, cargo="visitante"):
    print(f"Olá, {nome}! Você é {cargo}.")
apresentar("Willian", "desenvolvedor")
apresentar("João") # usa o padrão "visitante"

# Função normal
def calcular_area(largura, altura):
    return largura * altura

# O mesmo como método de uma classe (POO)
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self): # self = a função conhece a classe!
        retangulo = self.largura * self.altura
#        return self.largura * self.altura
        print(f"Sendo a largura {self.largura}m e a altura {self.altura}m o retângulo mede {retangulo}m².")
    
c1 = Retangulo(20, 30)
print(c1.calcular_area())