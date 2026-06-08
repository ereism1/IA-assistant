import re

def limpar_sql(sql):

    linhas = sql.split("\n")

    sql_limpo = []

    for linha in linhas:

        linha = linha.strip()

        if linha.upper() == "SQL:":
            continue

        if linha.startswith("```"):
            continue

        sql_limpo.append(linha)

    return "\n".join(sql_limpo)
