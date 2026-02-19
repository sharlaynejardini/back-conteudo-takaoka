# ==========================================
# DEFINIÇÃO DOS SCHEMAS (MODELOS Pydantic)
# ==========================================

from pydantic import BaseModel


# Schema base usado para criar ou atualizar conteúdo
class ConteudoBase(BaseModel):
    professor: str
    serie: str
    disciplina: str
    bimestre: int
    conteudo: str


# Schema usado para retornar dados ao cliente
class ConteudoResponse(ConteudoBase):
    id: str

    class Config:
        orm_mode = True  # Permite converter objeto SQLAlchemy para JSON
