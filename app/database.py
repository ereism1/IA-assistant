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
        return []

    return [
        dict(linha._mapping)
        for linha in resultado
    ]

def salvar_historico(pergunta, sql, resposta):

    with engine.connect() as conn:

        conn.execute(
            text("""
                INSERT INTO historico_consultas
                (
                    pergunta,
                    sql_gerada,
                    resposta_ia
                )
                VALUES
                (
                    :pergunta,
                    :sql,
                    :resposta
                )
            """),
            {
                "pergunta": pergunta,
                "sql": sql,
                "resposta": resposta
            }
        )

        conn.commit()

def listar_historico():

    with engine.connect() as conn:

        resultado = conn.execute(
            text("""
                SELECT
                    id,
                    pergunta,
                    sql_gerada,
                    resposta_ia,
                    data_consulta
                FROM historico_consultas
                ORDER BY data_consulta DESC
                LIMIT 100
            """)
        )

        return [
            dict(row._mapping)
            for row in resultado
        ]

def buscar_contexto(limite=5):

    with engine.connect() as conn:

        resultado = conn.execute(text("""
            SELECT pergunta, resposta_ia
            FROM historico_consultas
            ORDER BY id DESC
            LIMIT :limite
        """), {"limite": limite})

        return resultado.fetchall()
