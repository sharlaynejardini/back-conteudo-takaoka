# ==========================================
# SCHEMAS Pydantic
# ==========================================

from pydantic import BaseModel


# ==============================
# SCHEMAS DE LISTAGEM
# ==============================

class ProfessorSchema(BaseModel):
    id: str
    nome: str

    class Config:
        orm_mode = True


class TurmaSchema(BaseModel):
    id: str
    nome: str

    class Config:
        orm_mode = True


class DisciplinaSchema(BaseModel):
    id: str
    nome: str

    class Config:
        orm_mode = True


class AtribuicaoSchema(BaseModel):
    id: str
    professor: ProfessorSchema
    turma: TurmaSchema
    disciplina: DisciplinaSchema

    class Config:
        orm_mode = True


# ==============================
# SCHEMA PARA SALVAR CONTEÚDO
# ==============================

class ConteudoCreate(BaseModel):
    atribuicao_id: str
    bimestre: int
    conteudo: str


class ConteudoResponse(BaseModel):
    id: str
    atribuicao_id: str
    bimestre: int
    conteudo: str

    class Config:
        orm_mode = True
