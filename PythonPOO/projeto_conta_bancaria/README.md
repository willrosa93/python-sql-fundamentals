# 🏦 Projeto Conta Bancária

Sistema bancário em Python com **POO + PostgreSQL + Docker**, desenvolvido como projeto final da Fase 1 do Roadmap de Engenharia de Dados.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-0DB7ED?logo=docker&logoColor=white)

---

## 📋 O que o projeto faz

- Cria contas do tipo **Corrente** ou **Poupança**
- Realiza **depósito**, **saque** e **rendimento** com validações
- Persiste todas as operações no **PostgreSQL**
- Roda completamente em **Docker** — sem instalar nada na máquina

---

## 🧱 Arquitetura das Classes

```
ContaBancaria (ABC)         ← classe abstrata base
│   titular, saldo
│   depositar(), sacar()
│   render() ← abstrato
│
├── Conta_Corrente          ← herança + polimorfismo
│   render() → "sem rendimento"
│
└── Conta_Poupanca          ← herança + polimorfismo
    TAXA_RENDIMENTO = 0.5%
    render() → aplica rendimento após 30 dias
```

```
repositorio_contas.py       ← CRUD no PostgreSQL
conexao.py                  ← conexão via variáveis de ambiente
menu.py                     ← interface interativa no terminal
__main__.py                 ← ponto de entrada
```

---

## 🚀 Como executar com Docker (recomendado)

**Pré-requisito:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado.

```bash
# 1. Clonar o repositório
git clone git@github.com:willrosa93/python-sql-fundamentals.git
cd python-sql-fundamentals/PythonPOO/projeto_conta_bancaria

# 2. Subir o banco e a aplicação
docker-compose up -d postgres   # sobe só o banco primeiro
docker-compose run --rm app     # roda a aplicação interativa

# 3. Quando terminar, derrubar tudo
docker-compose down
```

> O banco de dados é criado automaticamente na primeira vez (`init.sql`).  
> Os dados **persistem** entre execuções graças ao volume `pg_data`.

---

## 🖥️ Como executar localmente (sem Docker)

**Pré-requisitos:** Python 3.11+ e PostgreSQL rodando localmente.

```bash
# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# edite o .env com suas credenciais

# Criar a tabela no banco
psql -U postgres -d banco_poo -f init.sql

# Rodar
python -m projeto_conta_bancaria
```

---

## 💡 Exemplo de uso

```
=== BANCO PYTHON ===
1 - Criar conta
2 - Depositar
3 - Sacar
4 - Listar contas
5 - Aplicar rendimento
0 - Sair

Escolha uma opção: 1

=== CRIAR CONTA ===
Nome do titular: Willian
Conta Corrente (C) ou Poupança (P)? P
Saldo inicial: 1000

Conta criada com sucesso!
ID da conta: 1
```

---

## 🔧 Stack utilizada

| Tecnologia | Uso |
|---|---|
| Python 3.11 | Linguagem principal |
| psycopg2 | Conexão com PostgreSQL |
| PostgreSQL 15 | Persistência dos dados |
| Docker + Compose | Ambiente isolado e reproduzível |
| ABC (abc module) | Classe abstrata `ContaBancaria` |

---

## 📚 Conceitos de POO aplicados

| Pilar | Implementação |
|---|---|
| **Encapsulamento** | `saldo` com validação, conexão isolada em `conexao.py` |
| **Herança** | `Conta_Corrente` e `Conta_Poupanca` herdam de `ContaBancaria` |
| **Polimorfismo** | `render()` se comporta diferente em cada tipo de conta |
| **Abstração** | `ContaBancaria(ABC)` com `@abstractmethod render()` |

---

## 👤 Autor

**Willian Rosa** — Analista de Banco de Dados em transição para Engenharia de Dados

[![GitHub](https://img.shields.io/badge/GitHub-willrosa93-black?logo=github)](https://github.com/willrosa93)