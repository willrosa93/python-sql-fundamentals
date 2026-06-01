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
from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Transporte(ABC):
    def __init__(self, dist):
        self.dist = dist

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, dist):
        super().__init__(dist)
        self.fator = 0.5

    def calc_frete(self):
        return self.dist * self.fator

class Caminhao(Transporte):
    def __init__(self, dist):
        super().__init__(dist)
        self.fator = 1.20

    def calc_frete(self):
        if self.dist > 10:
            return(f"Raio mínimo de 50km")
        else:
            return self.dist * self.fator
        
class Drone(Transporte):
    def __init__(self, dist):
        super().__init__(dist)
        self.fator = 9.50

    def calc_frete(self):
        if self.dist > 10:
            return(f"Raio máximo de 10km")
        else:
            return self.dist * self.fator
        