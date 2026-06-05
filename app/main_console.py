import time

from llm import gerar_sql
from database import executar_sql
from utils import limpar_sql

pergunta = input("Digite sua pergunta: ")

inicio = time.time()

sql_bruto = gerar_sql(pergunta)

sql = limpar_sql(sql_bruto)

resultado = executar_sql(sql)

fim = time.time()

tempo_total = round(fim - inicio, 2)

print("\n==========================")
print("PERGUNTA:")
print(pergunta)

print("\nSQL:")
print(sql)

print("\nRESULTADO:")
print(resultado)

print(f"\nTEMPO TOTAL: {tempo_total}s")
print("==========================")