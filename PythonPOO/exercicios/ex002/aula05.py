# Declaração de classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa use:
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "", idade = 0): # Método Construtor é o que define os atributos
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1
    
    def __str__(self): #Dunder method
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"
    

# Declaração de objetos
g1 = Gafanhoto("Maria", 17) #Chamada método construtor
g1.aniversario() #chama método de instancia
print(g1) #chama método de mensagem
print(g1.__class__) #chama método de mensagem

# segundo objeto
g2 = Gafanhoto("Willian", 99)
g2.aniversario()
print(g2)
print(g2.__getstate__())

# terceiro objeto
g3 = Gafanhoto("Peter",0)
g3.aniversario()
print(g3)

print(g1.__doc__)

print(g1)

print(g1.__dict__)

print(g1.__getstate__())