
# Crie uma classe chamada ControleRemoto, onde vamos simular um controle simples (canal, volume, liga/desliga)


# Etiqueta TV
# A TV está desligada

# Fora da etiqueta < CH1 > - VOL2 +

# @ liga

# etiqueta TV
# CANAL = 1 2 3 4 5 (destaca o canal em que está)
# VOLUME 
# < CH1 > - VOL2 +

# Se digitar @ desliga

# o programa tem que entender que não adianta aumentar o volume quando estiver 5 por exemplo

# 0 sai do programa
from rich import print
from rich.panel import Panel


class ControleRemoto:
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 2

    # Liga / Desliga
    def power(self):
        self.ligada = not self.ligada

    # Aumenta volume
    def aumentar_volume(self):
        if self.ligada:

            if self.volume < 5:
                self.volume += 1

            else:
                print("[red]Volume já está no máximo![/]")

    # Diminui volume
    def diminuir_volume(self):
        if self.ligada:

            if self.volume > 0:
                self.volume -= 1

            else:
                print("[red]Volume já está no mínimo![/]")

    # Próximo canal
    def proximo_canal(self):
        if self.ligada:

            if self.canal < 5:
                self.canal += 1

            else:
                self.canal = 1

    # Canal anterior
    def canal_anterior(self):
        if self.ligada:

            if self.canal > 1:
                self.canal -= 1

            else:
                self.canal = 5

    # Mostra status
    def etiqueta(self):

        if not self.ligada:

            painel = Panel(
                "[bold red]A TV está desligada[/]",
                title="📺 TV",
                border_style="red"
            )

        else:

            canais = ""

            for i in range(1, 6):

                if i == self.canal:
                    canais += f"[black on green] {i} [/] "
                else:
                    canais += f"{i} "

            painel = Panel(
                f"""
[bold cyan]CANAIS:[/]
{canais}

[bold yellow]VOLUME:[/] {self.volume}

[green]< CH+ >[/]
[green]< CH- >[/]

[magenta]< VOL+ >[/]
[magenta]< VOL- >[/]
                """,
                title="📺 TV",
                border_style="green"
            )

        print(painel)


# ======================
# PROGRAMA
# ======================

tv = ControleRemoto()

while True:

    tv.etiqueta()

    print("""
[@] Liga / Desliga
[1] Canal +
[2] Canal -
[3] Volume +
[4] Volume -
[0] Sair
""")

    opcao = input("Escolha: ")

    if opcao == "@":
        tv.power()

    elif opcao == "1":
        tv.proximo_canal()

    elif opcao == "2":
        tv.canal_anterior()

    elif opcao == "3":
        tv.aumentar_volume()

    elif opcao == "4":
        tv.diminuir_volume()

    elif opcao == "0":
        print("[bold red]Programa encerrado.[/]")
        break