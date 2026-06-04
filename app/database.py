from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    os.getenv("DATABASE_URL")
)

def executar_sql(sql):

    with engine.connect() as conn:

        resultado = conn.execute(text(sql))

        return resultado.fetchall()