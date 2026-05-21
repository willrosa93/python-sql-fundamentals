# Tupla com os dias úteis da semana
dias = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta")

print(dias[0]) # Segunda (índice começa em 0!)
print(dias[-1]) # Sexta (índice negativo = do final)
print(len(dias)) # 5 (quantidade de itens)

# Percorrendo a tupla com for
for di in dias:
    print(f"Dia: {di}")

numeros = (3, 7, 2, 9, 1)

print(min(numeros)) # 1 — menor valor
print(max(numeros)) # 9 — maior valor
print(sum(numeros)) # 22 — soma de tudo
# Verificando se um item está na tupla
print(7 in numeros) # True
print(2 in numeros) # False
# Contando ocorrências
notas = (7, 8, 7, 9, 7)
print(notas.count(9)) # 3 (o número 7 aparece 3 vezes)