
#Crie a classe Livro que vai simular a passagem de páginas de um livro.
#Considerando também se o usuário chegou ao fim da leitura.

# Crie a classe Livro que vai simular a passagem de páginas de um livro.
# Considerando também se o usuário chegou ao fim da leitura.

# Declaração da classe
class Livro:

    # Método construtor
    def __init__(self, nome, qtd_pag):
        self.nome = nome
        self.qtd_pag = qtd_pag
        self.pagina_atual = 0

        print(
            f"Você acabou de abrir o livro {self.nome} "
            f"que tem {self.qtd_pag} páginas no total. "
            f"Você está na página {self.pagina_atual}."
        )

    # Método de instância
    def avancar_paginas(self, qtd_lida):

        paginas = []

        # Avança página por página
        for i in range(qtd_lida):

            # Verifica se chegou ao final
            if self.pagina_atual >= self.qtd_pag:
                return (
                    f"Você terminou o livro {self.nome}! "
                    f"A última página foi a {self.qtd_pag}."
                )

            self.pagina_atual += 1
            paginas.append(f"Pág{self.pagina_atual}")

        caminho = " > ".join(paginas)

        # Mensagem normal
        if self.pagina_atual < self.qtd_pag:
            return (
                f"{caminho}: Você avançou {qtd_lida} páginas "
                f"e agora está na página {self.pagina_atual}."
            )

        # Mensagem ao finalizar
        else:
            return (
                f"{caminho}: Parabéns! Você terminou o livro "
                f"{self.nome} na página {self.qtd_pag}."
            )


# Criando objeto
l1 = Livro("10 coisas sobre Python", 20)

# Avançando páginas
print(l1.avancar_paginas(5))
print(l1.avancar_paginas(6))
print(l1.avancar_paginas(10))

#Se nao avançar e rodar o código:
#Você acabou de abrir o livro 10 coisas... que tem 20 páginas no total. Você está na página 1.


# Pág2 > Pág3 > Pág4 > Pág5 > Pág6: Você avançou 5 páginas e agora está na página 6.

#programa deve saber interpretar que o livro chegou ao fim