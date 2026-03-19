from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import criar_tabela, criar_post, listar_posts, delete_posts

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    criar_tabela()
    print("Banco pronto")

    yield

    print("Encerrando aplicação")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.post("/posts")
def add_post():
    criar_post("titulo teste", "conteudo teste")
    return {"msg": "post criado"}

@app.get("/list")
def get_posts():
    return listar_posts()

@app.delete("/delete")
def de():
    delete_posts()
    return {"msg": "todos os posts removidos"}