# ==========================================
# CAMADA DE ACESSO AO BANCO (CRUD)
# ==========================================

from sqlalchemy.orm import Session
import models


# ==========================================
# FUNÇÃO PARA BUSCAR CONTEÚDO
# ==========================================
def buscar_conteudo(db: Session, professor: str, serie: str, disciplina: str, bimestre: int):
    """
    Busca um conteúdo específico com base em:
    professor + série + disciplina + bimestre
    """
    return db.query(models.Conteudo).filter_by(
        professor=professor,
        serie=serie,
        disciplina=disciplina,
        bimestre=bimestre
    ).first()


# ==========================================
# FUNÇÃO PARA CRIAR OU ATUALIZAR CONTEÚDO
# ==========================================
def criar_ou_atualizar(db: Session, dados):
    """
    Se o conteúdo já existir, atualiza.
    Se não existir, cria um novo registro.
    """

    # Primeiro verifica se já existe registro
    conteudo_existente = buscar_conteudo(
        db,
        dados.professor,
        dados.serie,
        dados.disciplina,
        dados.bimestre
    )

    # Se existir → atualiza
    if conteudo_existente:
        conteudo_existente.conteudo = dados.conteudo
        db.commit()
        db.refresh(conteudo_existente)
        return conteudo_existente

    # Se não existir → cria novo
    novo = models.Conteudo(**dados.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo
