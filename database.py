# ==========================================
# CONFIGURAÇÃO DE CONEXÃO COM O BANCO
# ==========================================

# Importações necessárias do SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Importações para carregar variáveis de ambiente
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Recupera a URL do banco de dados definida no .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o mecanismo de conexão com o PostgreSQL (Supabase)
engine = create_engine(DATABASE_URL)

# Cria a fábrica de sessões (cada requisição terá sua própria sessão)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base usada para criar os modelos (tabelas)
Base = declarative_base()
