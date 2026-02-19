# ==========================================
# APLICAÇÃO PRINCIPAL FASTAPI
# ==========================================

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
import schemas
import crud

app = FastAPI(title="Sistema de Conteúdos Essenciais - Relacional")


# ==========================================
# DEPENDÊNCIA DE SESSÃO
# ==========================================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================================
# ENDPOINTS DE LISTAGEM
# ==========================================

@app.get("/professores", response_model=list[schemas.ProfessorSchema])
def get_professores(db: Session = Depends(get_db)):
    return crud.listar_professores(db)


@app.get("/turmas", response_model=list[schemas.TurmaSchema])
def get_turmas(db: Session = Depends(get_db)):
    return crud.listar_turmas(db)


@app.get("/atribuicoes/{professor_id}", response_model=list[schemas.AtribuicaoSchema])
def get_atribuicoes(professor_id: str, db: Session = Depends(get_db)):
    return crud.listar_atribuicoes_por_professor(db, professor_id)


# ==========================================
# ENDPOINTS DE CONTEÚDO
# ==========================================

@app.get("/conteudo")
def buscar_conteudo(atribuicao_id: str, bimestre: int, db: Session = Depends(get_db)):
    conteudo = crud.buscar_conteudo(db, atribuicao_id, bimestre)

    if not conteudo:
        raise HTTPException(status_code=404, detail="Conteúdo não encontrado")

    return conteudo


@app.post("/conteudo", response_model=schemas.ConteudoResponse)
def salvar_conteudo(dados: schemas.ConteudoCreate, db: Session = Depends(get_db)):
    return crud.criar_ou_atualizar_conteudo(db, dados)
