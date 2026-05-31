# implemente o seguinte diagrama de classes:

# poligono (abstract)
# qtd_lados
# perimetro() (abstract)
# area() (abstract)

# herdar de abc
# decorador abstractmethod
# implementação vazia (pass)

# Quadrado
# lado
# perimetro() (herdado da mãe)
# area() (herdado da mãe)

# Círculo
# raio
## perimetro() (herdado da mãe)
# area() (herdado da mãe)

# Quadrado e círculo
# Vão herdar qtd_lados, perímetros e área

from rich import print, inspect
from poligono import *

def main():
    p1 = Quadrado(12)

    print(f"Perímetro = {p1.perimetro():.1f}")
    print(f"Área = {p1.area():.1f}")

if __name__ == "__main__":
    main()