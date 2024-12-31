from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a URL do banco de dados da variável de ambiente
database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise ValueError("A variável de ambiente DATABASE_URL não foi definida.")

# Criar o engine do SQLAlchemy
engine = create_engine(database_url)


