# ==========================================
# MAIN - ARQUIVO PRINCIPAL DA API
# ==========================================

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models
import schemas
import crud

# 🔥 Instância principal da aplicação
app = FastAPI()

# 🔥 Criação automática das tabelas (caso não existam)
Base.metadata.create_all(bind=engine)


# ==========================================
# DEPENDÊNCIA DE BANCO
# ==========================================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================================
# LISTAR PROFESSORES
# ==========================================

@app.get("/professores", response_model=list[schemas.ProfessorResponse])
def get_professores(db: Session = Depends(get_db)):
    return crud.listar_professores(db)


# ==========================================
# LISTAR TURMAS
# ==========================================

@app.get("/turmas", response_model=list[schemas.TurmaResponse])
def get_turmas(db: Session = Depends(get_db)):
    return crud.listar_turmas(db)


# ==========================================
# LISTAR DISCIPLINAS
# ==========================================

@app.get("/disciplinas", response_model=list[schemas.DisciplinaResponse])
def get_disciplinas(db: Session = Depends(get_db)):
    return crud.listar_disciplinas(db)


# ==========================================
# LISTAR ATRIBUIÇÕES POR PROFESSOR
# ==========================================

@app.get("/atribuicoes/{professor_id}", response_model=list[schemas.AtribuicaoResponse])
def get_atribuicoes(professor_id: str, db: Session = Depends(get_db)):
    return crud.listar_atribuicoes_por_professor(db, professor_id)


# ==========================================
# SALVAR CONTEÚDO
# ==========================================

@app.post("/conteudos", response_model=schemas.ConteudoResponse)
def salvar_conteudo(dados: schemas.ConteudoCreate, db: Session = Depends(get_db)):
    return crud.salvar_conteudo(db, dados)
