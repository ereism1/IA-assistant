from ollama import chat
from prompts import SCHEMA

def gerar_sql(pergunta):

    prompt = f"""
    {SCHEMA}

    Pergunta:
    {pergunta}
    """

    response = chat(
        model="qwen3:4b",
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
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]