from fastapi import FastAPI
from app.llm import gerar_sql
from app.database import executar_sql, formatar_resultado
from app.utils import limpar_sql
from pydantic import BaseModel

app = FastAPI()

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

    sql_bruto = gerar_sql(req.pergunta)

    sql = limpar_sql(sql_bruto)

    resultado_bruto = executar_sql(sql)
    resultado = formatar_resultado(resultado_bruto)

    return {
    "pergunta": req.pergunta,
    "sql": sql,
    "resultado": {
        "produto": resultado[0],
        "valor": float(resultado[1]) if len(resultado) > 1 else None
    }
}