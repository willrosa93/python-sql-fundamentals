# Simule uma cafeteira orientada a objetos

# BebidaQuente (abstract)

# preparar()
# ferver_agua()
# misturar() (abstract)
# servir() (abstract)

# Cafe
# misturar() (abstract)
# servir() (abstract)

# Cha
# misturar() (abstract)
# servir() (abstract)

# Leite
# misturar() (abstract)
# servir() (abstract)

from cafeteria import *

def main():
    b1 = Cafe()
    b2 = Cha()
    b3 = Leite()
    b1.preparar()
    b2.preparar()
    b3.preparar()

if __name__ == "__main__":
    main()

# --- Iniciando o Preparo ---
# 1. Fervendo água a 100 graus Celsius.
# 2. Passando água pressurizada pelo pó de café moído.
# 3. Servindo em xícara pequena.
# --- Bebida Pronta ---

# Se for chá

# --- Iniciando o Preparo ---
# 1. Fervendo água a 100 graus Celsius.
# 2. Mergulhando o sachê de ervas na água.
# 3. Servindo na caneca de porcelana com limão.
# --- Bebida Pronta ---

# Se for Leite

# --- Iniciando o Preparo ---
# 1. Fervendo água a 100 graus Celsius.
# 2. Passando vapor pressurizada pelo bico do leite.
# 3. Servindo na caneca grande com café.
# --- Bebida Pronta ---

# tentar sem usar if