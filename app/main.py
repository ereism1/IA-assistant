from fastapi import FastAPI
from app.llm import gerar_sql, gerar_resposta
from app.database import executar_sql, formatar_resultado, salvar_historico, listar_historico, buscar_contexto
from app.utils import limpar_sql
from pydantic import BaseModel

app = FastAPI()

historico = buscar_contexto(10)

contexto = ""

for item in historico:

    contexto += f"""
Pergunta: {item[0]}
Resposta: {item[1]}
"""

class PerguntaRequest(BaseModel):
    pergunta: str

@app.get("/")
def home():

    return {
        "status": "online",
        "projeto": "Assistente SQL IA"
    }


@app.post("/pergunta")
def perguntar(req: PerguntaRequest):

    try:

        sql_bruto = gerar_sql(req.pergunta, contexto)

        sql = limpar_sql(sql_bruto)

        print("\n====================")
        print("PERGUNTA:")
        print(req.pergunta)
        print("\nSQL GERADA:")
        print(sql)
        print("====================\n")

        resultado_bruto = executar_sql(sql)

        resultado = formatar_resultado(resultado_bruto)

        resposta_ia = gerar_resposta(
               req.pergunta,
               resultado
         )

        salvar_historico(
               req.pergunta,
               sql,
               resposta_ia
         )

        return {
            "status": "sucesso",
            "pergunta": req.pergunta,
            "sql": sql,
            "resultado": resultado,
	    "resposta": resposta_ia
        }

    except Exception as e:

        return {
            "status": "erro",
            "pergunta": req.pergunta,
            "sql": sql if "sql" in locals() else None,
            "erro": str(e)
        }

@app.get("/historico")
def historico():

    return {
        "status": "sucesso",
        "historico": listar_historico()
    }
