# Criando uma lista (colchetes!)
compras = ["arroz", "feijão", "macarrão"]

# Adicionando itens
compras.append("café") # adiciona no final
compras.insert(1, "sal") # adiciona na posição 1

# Removendo itens
compras.remove("macarrão") # remove pelo valor
compras.pop() # remove o último
compras.pop() # remove o último
compras.pop(0) # remove o índice 0

# Alterando um item
compras[0] = "arroz integral"
print(compras)

notas = [7.5, 9.0, 6.0, 8.5, 5.0]

# Percorrendo
for nota in notas:
    print(f"Nota: {nota}")
# Ordenando (modifica a lista)
notas.sort()
print(notas) # [5.0, 6.0, 7.5, 8.5, 9.0]
notas.sort(reverse=True)
print(notas) # [9.0, 8.5, 7.5, 6.0, 5.0]
# Estatísticas
print(f"Maior: {max(notas)}")
print(f"Menor: {min(notas)}")
print(f"Média: {sum(notas) / len(notas):.1f}")