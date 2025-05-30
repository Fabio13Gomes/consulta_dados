import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()

# Configurações do banco
usuario = os.getenv("DB_USER")
senha = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
porta = os.getenv("DB_PORT")
banco = os.getenv("DB_NAME")
prefix = os.getenv("DB_PREFIX")

# Criação da engine de conexão
url = f'postgresql://{prefix}:{senha}@{host}:{porta}/{banco}'
engine = create_engine(url)

# Consulta SQL
consulta = "SELECT * FROM minha_tabela"
df = pd.read_sql(consulta, con=engine)

# Exibe os dados
print(df.head())

# (Opcional) salvar localmente
df.to_csv("dados_consultados.csv", index=False)
