import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

def get_connection():
    return sqlite3.connect(ROOT_PATH / "banco.db")