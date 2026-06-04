from database import executar_sql

resultado = executar_sql("""
SELECT COUNT(*)
FROM vendas_novo
""")

print(resultado)