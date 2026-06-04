from llm import gerar_sql
from database import executar_sql

pergunta = "Qual produto gerou maior faturamento?"

sql = gerar_sql(pergunta)

print("SQL GERADO:")
print(sql)

resultado = executar_sql(sql)

print("\nRESULTADO:")
print(resultado)