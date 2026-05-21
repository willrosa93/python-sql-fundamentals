import math
print(math.sqrt(81)) # 4.0 — raiz quadrada
print(math.pi) # 3.14159... — número pi
print(math.ceil(4.2)) # 5 — arredonda para cima
print(math.floor(4.8)) # 4 — arredonda para baixo
import random

# Número aleatório entre 1 e 10
numero = random.randint(1, 10)
print(f"Sorteio: {numero}")
# Escolher aleatoriamente de uma lista
frutas = ["maçã", "banana", "uva"]
escolha = random.choice(frutas)
print(f"Fruta sorteada: {escolha}")

# --------------------------------------------------------

from datetime import date, datetime
hoje = date.today()
print(f"Hoje: {hoje}") # 2026-05-19
print(f"Ano: {hoje.year}") # 2026
print(f"Mês: {hoje.month}") # 5
agora = datetime.now()
print(f"Agora: {agora.strftime('%H:%M')}")