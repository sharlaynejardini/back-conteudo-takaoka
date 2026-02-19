# ==========================================
# DEFINIÇÃO DO MODELO DA TABELA
# ==========================================

# Importações necessárias
from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

# Importa a Base criada no database.py
from database import Base


# Classe que representa a tabela "conteudos" no banco
class Conteudo(Base):
    __tablename__ = "conteudos"  # Nome da tabela no banco

    # ==========================================
    # COLUNAS DA TABELA
    # ==========================================

    # ID único gerado automaticamente (UUID)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Nome do professor
    professor = Column(String, nullable=False)

    # Série ou turma (ex: 2ºA)
    serie = Column(String, nullable=False)

    # Disciplina (ex: Português)
    disciplina = Column(String, nullable=False)

    # Bimestre (1, 2, 3 ou 4)
    bimestre = Column(Integer, nullable=False)

    # Texto do conteúdo essencial
    conteudo = Column(Text, nullable=False)

    # Data de criação automática
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Data de última atualização automática
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(),
                        onupdate=func.now())
