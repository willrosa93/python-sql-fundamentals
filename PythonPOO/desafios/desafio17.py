from rich import print
from rich.panel import Panel
from rich.align import Align

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
 
    def etiqueta(self):

        texto = f"[bold]{self.nome}[/bold]\nR$ {self.preco}"

        painel = Panel(
            Align.center(texto),
            title="PRODUTO",
            width=30,
            border_style="green"
        )

        print(painel)

c1 = Produto("Iphone 8", "800,00")
c2 = Produto("Mouse", "120,00")
print(c1.etiqueta())
print(c2.etiqueta())