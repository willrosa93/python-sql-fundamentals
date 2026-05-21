# Criando um dicionário (chave: valor)
pessoa = {
"nome": "Willian",
"idade": 30,
"cidade": "São Paulo"
}
# Acessando valores
print(pessoa["nome"]) # Willian
print(pessoa["idade"]) # 30
# Adicionando / alterando
pessoa["email"] = "w@email.com" # nova chave
pessoa["idade"] = 31 # altera existente
# Removendo
del pessoa["cidade"]
print(pessoa)

aluno = {"nome": "Ana", "nota": 9.5, "turma": "A"}
# Percorrendo chaves e valores juntos
for chaves, valores in aluno.items():
    print(f"{chaves}: {valores}")
# Acessando com segurança (sem erro se chave não existir)
print(aluno.get("email", "w@email.com"))