contador = 1

while contador <= 5:
    print(f"Contando: {contador}")
    contador += 4 # IMPORTANTE: nunca esqueça de atualizar!

print("Acabou!")

# Fica pedindo a nota até o usuário digitar algo válido
nota = float(input("Digite uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida! Tente novamente.")
    nota = float(input("Digite uma nota de 0 a 10: "))
print(f"Nota registrada: {nota}")