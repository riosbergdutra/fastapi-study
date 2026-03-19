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
