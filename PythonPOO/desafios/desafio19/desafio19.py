from rich import print 
import time 

#Crie a classe Livro que vai simular a passagem de páginas de um livro.
#Considerando também se o usuário chegou ao fim da leitura.

# Crie a classe Livro que vai simular a passagem de páginas de um livro.
# Considerando também se o usuário chegou ao fim da leitura.

# Declaração da classe
class Livro:

    # Método construtor
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(
            f":open_book: [blue]Você acabou de abrir o livro [red]{self.titulo} [/]"
            f"que tem {self.total_paginas} páginas [/]no total. "
            f"Você está na [yellow]página {self.pagina_atual}[/]."
        )

    # Método de instância
    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward:", end='')
                time.sleep(0.2)
                cont += 1

        print(f"[blue]Você avançou {cont} páginas e agora está na [yellow]página {self.pagina_atual}[/][/blue]") 
        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro {self.titulo}[/]")

    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False      
#           return True self.pagina_atual == self.total_paginas else False

# Criando objeto
l1 = Livro("10 coisas sobre Python", 20)

# Avançando páginas
print(l1.avancar_paginas(20))
#print(l1.avancar_paginas(6))
#print(l1.avancar_paginas(10))

#Se nao avançar e rodar o código:
#Você acabou de abrir o livro 10 coisas... que tem 20 páginas no total. Você está na página 1.


# Pág2 > Pág3 > Pág4 > Pág5 > Pág6: Você avançou 5 páginas e agora está na página 6.

#programa deve saber interpretar que o livro chegou ao fim