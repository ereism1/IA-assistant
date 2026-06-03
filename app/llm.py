from ollama import chat

response = chat(
    model='qwen3:4b',
    messages=[
        {
            'role': 'user',
            'content': '''
Você é especialista em PostgreSQL.

Tabelas:

clientes(
id,
nome,
cidade
)

vendas(
id,
cliente_id,
valor,
data_venda
)

Gere apenas SQL.

Pergunta:
Qual cliente possui maior faturamento?
'''
        }
    ]
)

print(response['message']['content'])