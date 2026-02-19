# ==========================================
# CAMADA DE ACESSO AO BANCO
# ==========================================

from sqlalchemy.orm import Session
import models


# ==========================================
# LISTAGENS
# ==========================================

def listar_professores(db: Session):
    return db.query(models.Professor).order_by(models.Professor.nome).all()


def listar_turmas(db: Session):
    return db.query(models.Turma).order_by(models.Turma.nome).all()


def listar_atribuicoes_por_professor(db: Session, professor_id: str):
    return db.query(models.Atribuicao).filter_by(professor_id=professor_id).all()


# ==========================================
# CONTEÚDO
# ==========================================

def buscar_conteudo(db: Session, atribuicao_id: str, bimestre: int):
    return db.query(models.Conteudo).filter_by(
        atribuicao_id=atribuicao_id,
        bimestre=bimestre
    ).first()


def criar_ou_atualizar_conteudo(db: Session, dados):
    existente = buscar_conteudo(db, dados.atribuicao_id, dados.bimestre)

    if existente:
        existente.conteudo = dados.conteudo
        db.commit()
        db.refresh(existente)
        return existente

    novo = models.Conteudo(**dados.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo
def salvar_conteudo(db, dados):
    conteudo = db.query(models.Conteudo).filter(
        models.Conteudo.atribuicao_id == dados.atribuicao_id,
        models.Conteudo.bimestre == dados.bimestre
    ).first()

    if conteudo:
        conteudo.conteudo = dados.conteudo
        conteudo.data_avaliacao = dados.data_avaliacao
    else:
        conteudo = models.Conteudo(
            atribuicao_id=dados.atribuicao_id,
            bimestre=dados.bimestre,
            conteudo=dados.conteudo,
            data_avaliacao=dados.data_avaliacao
        )
        db.add(conteudo)

    db.commit()
    db.refresh(conteudo)
    return conteudo
