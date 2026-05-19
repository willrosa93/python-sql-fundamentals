# Declaração de classe
class Gafanhoto:
    def __init__(self): # Método Construtor é o que define os atributos
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."
    

# Declaração de objetos
g1 = Gafanhoto() #Chamada método construtor
g1.nome = "Maria" #Atribui nome
g1.idade = 18 #atribui idade
g1.aniversario() #chama método de instancia
print(g1.mensagem()) #chama método de mensagem

# segundo objeto
g2 = Gafanhoto()
g2.nome = "Willian"
g2.idade = 99
g2.aniversario()
print(g2.mensagem())

# terceiro objeto
g3 = Gafanhoto()
g3.nome = "Peter"
g3.idade = 0
g3.aniversario()
print(g3.mensagem())