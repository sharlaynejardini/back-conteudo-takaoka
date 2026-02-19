# ==========================================
# SCHEMAS PYDANTIC
# ==========================================

from pydantic import BaseModel
from uuid import UUID
from datetime import date


# ==========================================
# PROFESSOR
# ==========================================

class ProfessorResponse(BaseModel):
    id: UUID
    nome: str

    class Config:
        from_attributes = True


# ==========================================
# TURMA
# ==========================================

class TurmaResponse(BaseModel):
    id: UUID
    nome: str

    class Config:
        from_attributes = True


# ==========================================
# DISCIPLINA
# ==========================================

class DisciplinaResponse(BaseModel):
    id: UUID
    nome: str

    class Config:
        from_attributes = True


# ==========================================
# ATRIBUIÇÃO
# ==========================================

class AtribuicaoResponse(BaseModel):
    id: UUID
    turma: TurmaResponse
    disciplina: DisciplinaResponse

    class Config:
        from_attributes = True


# ==========================================
# CONTEÚDO
# ==========================================

class ConteudoCreate(BaseModel):
    atribuicao_id: UUID
    bimestre: int
    conteudo: str
    data_avaliacao: date   # 🔥 AGORA OBRIGATÓRIA


class ConteudoResponse(BaseModel):
    id: UUID
    atribuicao_id: UUID
    bimestre: int
    conteudo: str
    data_avaliacao: date

    class Config:
        from_attributes = True
