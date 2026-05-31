# Simule o sistema de batalha enter personagens de um RPG

# Personagem(abstract)
# nome
# vida
# golpes
# atacar(alvo, forca)
# receber_dano(dano)
# curar() (abstract)

# Guerreiro
# curar()

# Mago
# curar()

from personagens_rpg import *

def main():
    p1 = Guerreiro("Kratos", 2000)
    p2 = Mago("Merlon", 3000)

    p1.atacar(p2, 1000)

if __name__ == "__main__":
    main()

# Kratos (2000) atacou Merlin(3000) com um Soco de força 1000
# Merlin recebeu dano de 602!

# cada vez que executar por mudar o golpe

# Kratos (2000) atacou Merlin(3000) com um Pulo Giratório de força 1000
# Merlin recebeu dano de 788!

# Kratos (2000) atacou Merlin(3000) com um Pulo Giratório de força 1000
# Merlin recebeu dano de 206!

# abaixo de     p1.atacar(p2, 1000)
    p2.curar()

# Merlin fez uma magia de cura e recuperou 7 pontos de vida.

    p2.atacar(p1, 20000)

# Merlin(2745) atacou Kratos(2000) com um Bola de Fogo de força 20000
# Kratos recebeu dano de 7834!

    p1.curar()
# Kratos enrolou uma atadura nos ferimentos e recuperu 5 pontos de vida.