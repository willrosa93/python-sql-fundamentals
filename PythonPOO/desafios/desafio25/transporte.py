# Crie classes capazes de calcular frete de veículos diferentes

# Transporte (abstract)
# distanciaancia
# frete
# calcular_frete() (abstract)

# Moto
# fator = 0.50
# calcular_frete() 
# Livre (nao importa distanciaância)

# Caminhao
# fator = 1.20
# calcular_frete() 
# Mínimo 50km

# Drone
# fator = 9.50
# calcular_frete() 
# Máximo 10km
from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass

class Moto(Transporte):
    fator = 0.5
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        self.frete = self.distancia * Moto.fator
        return f"R${self.frete:,.2f}"

class Caminhao(Transporte):
        fator = 1.20
        def __init__(self, distancia):
            super().__init__(distancia)


        def calcular_frete(self):
            if self.distancia < 50:
                return(f"Raio mínimo de 50km")
            else:
                self.frete = self.distancia * Caminhao.fator
                return f"R${self.frete:,.2f}"

class Drone(Transporte):
        fator = 9.50
        def __init__(self, distancia):
            super().__init__(distancia)

        def calcular_frete(self):
            if self.distancia > 10:
                return(f"Raio máximo de 10km")
            else:
                self.frete = self.distancia * Drone.fator
                return f"R${self.frete:,.2f}"            