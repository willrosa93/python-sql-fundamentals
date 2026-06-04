import os
import psycopg2


def conectar():

    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "banco_poo"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "123456")
    )

    cur = conn.cursor()

    cur.execute("SELECT current_database();")
    print("Banco conectado:", cur.fetchone()[0])

    cur.execute("SELECT current_schema();")
    print("Schema:", cur.fetchone()[0])

    cur.close()

    return conn
