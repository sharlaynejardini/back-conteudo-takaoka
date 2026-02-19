# ==========================================
# APLICAÇÃO PRINCIPAL FASTAPI
# ==========================================

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

# Importações internas
from database import SessionLocal
import schemas
import crud

# ==========================================
# CRIAÇÃO DA APLICAÇÃO
# ==========================================

app = FastAPI(title="Sistema de Conteúdos Essenciais")


# ==========================================
# DEPENDÊNCIA PARA GERENCIAR SESSÃO DO BANCO
# ==========================================
def get_db():
    """
    Cria uma sessão de banco para cada requisição.
    Fecha automaticamente ao final.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================================
# ENDPOINT PARA BUSCAR CONTEÚDO
# ==========================================
@app.get("/conteudo")
def buscar_conteudo(
    professor: str,
    serie: str,
    disciplina: str,
    bimestre: int,
    db: Session = Depends(get_db)
):
    """
    Busca conteúdo existente com base nos filtros informados.
    """

    conteudo = crud.buscar_conteudo(
        db,
        professor,
        serie,
        disciplina,
        bimestre
    )

    if not conteudo:
        raise HTTPException(status_code=404, detail="Conteúdo não encontrado")

    return conteudo


# ==========================================
# ENDPOINT PARA CRIAR OU ATUALIZAR CONTEÚDO
# ==========================================
@app.post("/conteudo")
def salvar_conteudo(
    dados: schemas.ConteudoBase,
    db: Session = Depends(get_db)
):
    """
    Cria novo conteúdo ou atualiza se já existir.
    """

    return crud.criar_ou_atualizar(db, dados)
