import re

def limpar_sql(sql):

    # remove blocos markdown
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    # remove espaços extras
    sql = sql.strip()

    return sql