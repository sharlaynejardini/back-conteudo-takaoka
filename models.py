# ==========================================
# DEFINIÇÃO DOS MODELOS RELACIONAIS
# ==========================================

from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from database import Base


# ==========================================
# TABELA PROFESSORES
# ==========================================
class Professor(Base):
    __tablename__ = "professores"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String, nullable=False, unique=True)


# ==========================================
# TABELA TURMAS
# ==========================================
class Turma(Base):
    __tablename__ = "turmas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String, nullable=False, unique=True)


# ==========================================
# TABELA DISCIPLINAS
# ==========================================
class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String, nullable=False, unique=True)


# ==========================================
# TABELA ATRIBUIÇÕES
# Define qual professor leciona qual disciplina em qual turma
# ==========================================
class Atribuicao(Base):
    __tablename__ = "atribuicoes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    professor_id = Column(UUID(as_uuid=True), ForeignKey("professores.id"))
    turma_id = Column(UUID(as_uuid=True), ForeignKey("turmas.id"))
    disciplina_id = Column(UUID(as_uuid=True), ForeignKey("disciplinas.id"))

    professor = relationship("Professor")
    turma = relationship("Turma")
    disciplina = relationship("Disciplina")


# ==========================================
# TABELA CONTEÚDOS
# ==========================================
class Conteudo(Base):
    __tablename__ = "conteudos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    atribuicao_id = Column(UUID(as_uuid=True), ForeignKey("atribuicoes.id"))
    bimestre = Column(Integer, nullable=False)
    conteudo = Column(Text, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(),
                        onupdate=func.now())

    atribuicao = relationship("Atribuicao")
