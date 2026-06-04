from llm import gerar_sql, gerar_resposta
from database import executar_sql
from utils import limpar_sql



pergunta = "Qual produto gerou maior faturamento?"

sql = gerar_sql(pergunta)

print("\nSQL GERADO:")
print(sql)

resultado = executar_sql(sql)

print("\nRESULTADO BRUTO:")
print(resultado)

resposta = gerar_resposta(pergunta, resultado)

print("\nRESPOSTA FINAL:")
print(resposta)


sql = gerar_sql(pergunta)

sql = limpar_sql(sql)