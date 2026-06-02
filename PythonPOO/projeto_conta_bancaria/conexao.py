import psycopg2


def conectar():

    conn = psycopg2.connect(
        host="localhost",
        database="banco_poo",
        user="postgres",
        password="123456"
    )

    cur = conn.cursor()

    cur.execute(
        "SELECT current_database();"
    )

    print(
        "Banco conectado:",
        cur.fetchone()[0]
    )

    cur.execute(
        "SELECT current_schema();"
    )

    print(
        "Schema:",
        cur.fetchone()[0]
    )

    cur.close()

    return conn