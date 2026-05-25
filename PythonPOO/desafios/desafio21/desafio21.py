from rich import print

# Crie a classe Caneta, que simule o funcionamento de uma caneta colorida,
# podendo escrever frases na cor relativa.
# Faz cores azul, vermelho e verde.

class Caneta:

    def __init__(self, cor):

        # Cores permitidas
        cores_validas = ["azul", "vermelho", "verde"]

        # Verifica se a cor é válida
        if cor not in cores_validas:
            print(f":x: A cor {cor} não é permitida.")
            return

        self.cor = cor
        self.status = "tampada"

    def destampar(self):

        if self.status == "destampada":
            print(f"A caneta {self.cor} já está destampada.")

        else:
            self.status = "destampada"
            print(f"A caneta {self.cor} foi destampada.")

    def tampar(self):

        if self.status == "tampada":
            print(f"A caneta {self.cor} já está tampada.")

        else:
            self.status = "tampada"
            print(f"A caneta {self.cor} foi tampada.")

    def escrever(self, frase):

        if self.status == "tampada":
            print(f":x: A caneta {self.cor} está tampada!")

        else:

            # Tradução das cores
            cores = {
                "azul": "blue",
                "vermelho": "red",
                "verde": "green"
            }

            cor_rich = cores[self.cor]

            print(f"[{cor_rich}]{frase}[/]")


c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("verde")
c4 = Caneta("roxo")  # cor inválida

c1.destampar()
c1.escrever("Olá, tudo bem?")

c2.destampar()
c2.escrever("Estou escrevendo em vermelho.")

c3.destampar()
c3.escrever("Agora estou escrevendo em verde.")