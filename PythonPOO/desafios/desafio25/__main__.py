# Crie classes capazes de calcular frete de veículos diferentes

# Transporte (abstract)
# distancia
# frete
# calc_frete() (abstract)

# Moto
# fator = 0.50
# calc_frete() 
# Livre (nao importa distância)

# Caminhao
# fator = 1.20
# calc_frete() 
# Mínimo 50km

# Drone
# fator = 9.50
# calc_frete() 
# Máximo 10km

from transporte import *
from rich import print, inspect 
from rich.table import Table

def main():
    dist = 5

    viagens = [Moto(dist), Caminhao(dist), Drone(dist)]
    """entrega = Caminhao(dist)
    print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_frete()}")"""

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    for item in viagens:
        tabela.add_row(f"{dist}Km",f"{type(item).__name__}",f"{item.calcular_frete()}")

    print(tabela)

if __name__ == "__main__":
    main()

# Frete de Moto em 20Km = R$10.00
# Frete de Caminhão em 20Km = Raio mínimo de 50km

# Mudando dist para 80
# Frete de Caminhão em 80Km = R$96.00

# Frete de Drone em 80Km = Raio mínimo de 10km
# Frete de Drone em 8Km = R$x

# Extra
# Entregar como tabela
# Tabela de Fretes
# equiparando os fretes em diferentes veículos

# def main():
    # dist = 100

    # viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

