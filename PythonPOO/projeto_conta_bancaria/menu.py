from conta_bancaria import (
    Conta_Corrente,
    Conta_Poupanca
)

from repositorio_contas import (
    salvar,
    buscar_por_id,
    atualizar,
    listar
)


def criar_conta():

    print("\n=== CRIAR CONTA ===")

    titular = input(
        "Nome do titular: "
    )

    tipo = input(
        "Conta Corrente (C) ou Poupança (P)? "
    ).upper()

    saldo = float(
        input(
            "Saldo inicial: "
        )
    )

    if tipo == "C":

        conta = Conta_Corrente(
            titular,
            saldo
        )

    elif tipo == "P":

        conta = Conta_Poupanca(
            titular,
            saldo
        )

    else:

        print("Tipo inválido.")
        return

    salvar(conta)

    print(
        f"\nConta criada com sucesso!"
    )

    print(
        f"ID da conta: {conta.id}"
    )


def depositar():

    print("\n=== DEPÓSITO ===")

    id_conta = int(
        input(
            "ID da conta: "
        )
    )

    valor = float(
        input(
            "Valor do depósito: "
        )
    )

    conta = buscar_por_id(
        id_conta
    )

    if conta is None:

        print(
            "Conta não encontrada."
        )

        return

    conta.depositar(valor)

    atualizar(conta)


def sacar():

    print("\n=== SAQUE ===")

    id_conta = int(
        input(
            "ID da conta: "
        )
    )

    valor = float(
        input(
            "Valor do saque: "
        )
    )

    conta = buscar_por_id(
        id_conta
    )

    if conta is None:

        print(
            "Conta não encontrada."
        )

        return

    conta.sacar(valor)

    atualizar(conta)


def listar_contas():

    print("\n=== CONTAS CADASTRADAS ===\n")

    contas = listar()

    if len(contas) == 0:

        print(
            "Nenhuma conta cadastrada."
        )

        return

    for conta in contas:

        print(
            f"ID: {conta[0]}"
        )

        print(
            f"Titular: {conta[1]}"
        )

        print(
            f"Saldo: R${conta[2]}"
        )

        print(
            f"Tipo: {conta[3]}"
        )

        print("-" * 40)


def aplicar_rendimento():

    print(
        "\n=== RENDIMENTO ==="
    )

    id_conta = int(
        input(
            "ID da conta: "
        )
    )

    conta = buscar_por_id(
        id_conta
    )

    if conta is None:

        print(
            "Conta não encontrada."
        )

        return

    conta.render()

    atualizar(conta)


def executar():

    while True:

        print(
            "\n=== BANCO PYTHON ==="
        )

        print(
            "1 - Criar conta"
        )

        print(
            "2 - Depositar"
        )

        print(
            "3 - Sacar"
        )

        print(
            "4 - Listar contas"
        )

        print(
            "5 - Aplicar rendimento"
        )

        print(
            "0 - Sair"
        )

        opcao = input(
            "\nEscolha uma opção: "
        )

        if opcao == "1":

            criar_conta()

        elif opcao == "2":

            depositar()

        elif opcao == "3":

            sacar()

        elif opcao == "4":

            listar_contas()

        elif opcao == "5":

            aplicar_rendimento()

        elif opcao == "0":

            print(
                "\nEncerrando sistema..."
            )

            break

        else:

            print(
                "\nOpção inválida."
            )