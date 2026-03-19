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


def criar_post(titulo, conteudo):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO posts (titulo, conteudo) VALUES (?, ?)",
        (titulo, conteudo)
    )

    conn.commit()
    conn.close()


def listar_posts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts")
    rows = cursor.fetchall()

    conn.close()

    posts = []
    for row in rows:
        posts.append({
            "id": row[0],
            "titulo": row[1],
            "conteudo": row[2]
        })

    return posts


def delete_posts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM posts")

    conn.commit()
    conn.close()