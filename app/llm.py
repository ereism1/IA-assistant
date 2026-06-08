from ollama import chat
from app.prompts import SCHEMA

def gerar_sql(pergunta, contexto=""):

    prompt = f"""
     {SCHEMA}

     Contexto da conversa:
     {contexto}

     Pergunta atual:
     {pergunta}

     Gere apenas SQL PostgreSQL.
     """

    response = chat(
        model="qwen2.5:1.5b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def gerar_resposta(pergunta, resultado):

    prompt = f"""
    Você é um analista de negócios.

    Pergunta:
    {pergunta}

    Resultado da consulta:
    {resultado}

    Gere uma resposta curta e amigável.
    Não invente informações.
    """

    response = chat(
        model="qwen2.5:1.5b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
