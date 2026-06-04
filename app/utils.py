def limpar_sql(sql):

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()