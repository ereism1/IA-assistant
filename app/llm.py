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

