from abc import ABC, abstractmethod
from random import choice, randint


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca):
        golpe = choice(self.golpes)
        dano = randint(1, forca)

        print(
            f"{self.nome} ({self.vida}) atacou "
            f"{alvo.nome} ({alvo.vida}) com um "
            f"{golpe} de força {forca}"
        )

        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida -= dano

        print(f"{self.nome} recebeu dano de {dano}!")

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

        self.golpes = [
            "Soco",
            "Chute",
            "Pulo Giratório",
            "Machadada"
        ]

    def curar(self):
        cura = randint(1, 10)

        self.vida += cura

        print(
            f"{self.nome} enrolou uma atadura "
            f"nos ferimentos e recuperou "
            f"{cura} pontos de vida."
        )

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

        self.golpes = [
            "Bola de Fogo",
            "Raio Arcano",
            "Tempestade Elétrica",
            "Explosão de Gelo"
        ]

    def curar(self):
        cura = randint(1, 10)

        self.vida += cura

        print(
            f"{self.nome} fez uma magia de cura "
            f"e recuperou {cura} pontos de vida."
        )