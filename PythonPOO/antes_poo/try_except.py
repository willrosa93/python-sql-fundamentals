try:
# Código que pode dar erro
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
    print(f"100 / {numero} = {resultado}")

except ValueError:
# Usuário digitou uma letra
    print("Erro: você precisava digitar um número!")

except ZeroDivisionError:
# Usuário digitou zero
    print("Erro: não é possível dividir por z")

try:
 idade = int(input("Sua idade: "))

except ValueError:
    print("Isso não é uma idade válida!")

else:
# Só executa se NÃO houve erro
    print(f"Você tem {idade} anos.")

finally:
# Executa SEMPRE, com ou sem erro
    print("Programa finalizado.")
