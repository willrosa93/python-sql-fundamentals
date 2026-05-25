# Crie a classe Gamer onde possa cadastrar nome, nick e jogos favoritos.

# Crie método que permita mostrar a ficha do gamer

# Adicionar emojis na lista
from rich import print
from rich.panel import Panel
from rich import inspect

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    # Mostra a ficha do gamer


     # Mostra a ficha
    def ficha(self):
        conteudo = f"Nome real: [black on blue] {self.nome} [/]"
        conteudo += f"\nJogos favoritos:"
        for num, game in enumerate(self.favoritos): 
            conteudo += f"\n:video_game: [blue] {game}[/]"
        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        print(painel)



# Criando gamer
j1 = Gamer("Fabricio da Silva", "detonator2025")

# Adicionando jogos
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
#inspect(j1)

j2 = Gamer("Willian Silva da Rosa", "rachacuca")

# Adicionando jogos
j2.add_favoritos("Pubg")
j2.add_favoritos("RE 4")

# Exibindo ficha
j1.ficha()
j2.ficha()

#Imprime etiqueta
# Nome real:
# Nick:
# Jogos favoritos:
#Lista