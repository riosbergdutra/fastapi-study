import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


def get_connection():
    return sqlite3.connect(ROOT_PATH / "banco.db")


def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()

    print("Criando tabela...")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        conteudo TEXT
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM posts")
    quantidade = cursor.fetchone()[0]


    if quantidade == 0:
        cursor.execute(
        "INSERT INTO posts (titulo, conteudo) VALUES (?, ?)",
        ("Primeiro post", "Conteúdo inicial")
    )

    conn.commit()
    conn.close()


