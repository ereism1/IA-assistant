from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    os.getenv("DATABASE_URL")
)

def validar_sql(sql):

    comandos_proibidos = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER",
        "TRUNCATE"
    ]

    sql_upper = sql.upper()

    for comando in comandos_proibidos:

        if comando in sql_upper:
            raise Exception(
                f"Comando proibido detectado: {comando}"
            )


def executar_sql(sql):

    with engine.connect() as conn:

        validar_sql(sql)

        resultado = conn.execute(text(sql))

        return resultado.fetchall()
    
def formatar_resultado(resultado):

    if not resultado:
        return None

    linha = resultado[0]

    return linha        
