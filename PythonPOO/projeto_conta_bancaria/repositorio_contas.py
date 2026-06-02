from conta_bancaria import (
    Conta_Corrente,
    Conta_Poupanca
)

from conexao import conectar


def salvar(conta):

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            current_database(),
            current_schema()
    """)

    print(cur.fetchone())

    cur.execute("""
        SELECT tablename
        FROM pg_tables
        WHERE schemaname = 'public'
    """)

    print(cur.fetchall())

    cur.execute(
        """
        INSERT INTO contas
        (
            titular,
            saldo,
            tipo,
            data_ultimo_deposito,
            data_ultimo_rendimento
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s
        )
        RETURNING id
        """,
        (
            conta.titular,
            conta.saldo,
            conta.__class__.__name__,
            conta.data_ultimo_deposito,
            conta.data_ultimo_rendimento
        )
    )

    conta.id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()


def buscar_por_id(id_conta):

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            id,
            titular,
            saldo,
            tipo,
            data_ultimo_deposito,
            data_ultimo_rendimento
        FROM contas
        WHERE id = %s
        """,
        (id_conta,)
    )

    dados = cur.fetchone()

    cur.close()
    conn.close()

    if dados is None:
        return None

    (
        id,
        titular,
        saldo,
        tipo,
        data_ultimo_deposito,
        data_ultimo_rendimento
    ) = dados

    if tipo == "Conta_Corrente":

        conta = Conta_Corrente(
            titular,
            saldo,
            data_ultimo_deposito,
            data_ultimo_rendimento
        )

    else:

        conta = Conta_Poupanca(
            titular,
            saldo,
            data_ultimo_deposito,
            data_ultimo_rendimento
        )

    conta.id = id

    return conta


def atualizar(conta):

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE contas
        SET
            saldo = %s,
            data_ultimo_deposito = %s,
            data_ultimo_rendimento = %s
        WHERE id = %s
        """,
        (
            conta.saldo,
            conta.data_ultimo_deposito,
            conta.data_ultimo_rendimento,
            conta.id
        )
    )

    conn.commit()

    cur.close()
    conn.close()


def listar():

    conn = conectar()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            id,
            titular,
            saldo,
            tipo
        FROM contas
        ORDER BY id
        """
    )

    contas = cur.fetchall()

    cur.close()
    conn.close()

    return contas