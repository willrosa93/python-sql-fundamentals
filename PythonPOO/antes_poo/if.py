# Imagine que você quer classificar a nota de um aluno
nota = 4
if nota >= 9:
    print("Excelente! Nota A")
elif nota >= 7:
    print("Bom! Nota B")
elif nota >= 5:
    print("Regular. Nota C")
else:
    print("Reprovado. Nota D")

imc = float(input("Qual o seu IMC? "))
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal — parabéns!")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")