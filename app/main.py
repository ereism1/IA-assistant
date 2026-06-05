from fastapi import FastAPI
from llm import gerar_sql
from database import executar_sql
from utils import limpar_sql

app = FastAPI()


@app.get("/")
def home():

    return {
        "status": "online",
        "projeto": "Assistente SQL IA"
    }


@app.post("/pergunta")
def perguntar(pergunta: str):

    sql_bruto = gerar_sql(pergunta)

    sql = limpar_sql(sql_bruto)

    resultado = executar_sql(sql)

    return {
        "pergunta": pergunta,
        "sql": sql,
        "resultado": str(resultado)
    }