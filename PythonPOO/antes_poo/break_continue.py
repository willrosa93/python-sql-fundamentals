# break → sai do loop imediatamente
for i in range(10):
    if i == 6:
        break
    print(i, end=" ")
# saída: 0 1 2 3 4


# continue → pula para a próxima repetição
for i in range(6):
    if i == 4:
        continue
    print(i, end=" ")