SCHEMA = """
Banco PostgreSQL.

Tabelas:

clientes (
    id,
    nome,
    tipo_pessoa
)

produtos (
    id,
    nome,
    preco
)

formas_pagamento (
    id,
    descricao
)

vendas_novo (
    id,
    cliente_id,
    produto_id,
    forma_pagamento_id,
    quantidade,
    valor,
    data_venda
)

Relacionamentos:

vendas_novo.cliente_id = clientes.id

vendas_novo.produto_id = produtos.id

vendas_novo.forma_pagamento_id = formas_pagamento.id


REGRAS OBRIGATÓRIAS:

- Gere SOMENTE SQL PostgreSQL
- Não explique nada
- Não use markdown
- Retorne apenas SQL
- Utilize SEMPRE:
    vendas_novo vn
    clientes c
    produtos p
    formas_pagamento fp

- Nunca utilize aliases diferentes
- Nunca utilize tabelas inexistentes
- Nunca utilize colunas inexistentes

REGRAS IMPORTANTES:

- Nunca faça GROUP BY em colunas numéricas usadas em SUM()
- Nunca faça GROUP BY em valor, preco, quantidade ou faturamento
- Ao calcular faturamento por produto use:

GROUP BY p.nome

- Ao calcular vendas por cliente use:

GROUP BY c.nome

- Ao calcular vendas por forma de pagamento use:

GROUP BY fp.descricao

Exemplo:

SELECT
    p.nome,
    SUM(vn.valor) AS total_faturado
FROM vendas_novo vn
JOIN produtos p
    ON vn.produto_id = p.id
GROUP BY p.nome
ORDER BY total_faturado DESC
LIMIT 5;

Pergunta:
Liste os 5 produtos mais vendidos

SQL:
SELECT
    p.nome,
    SUM(vn.quantidade) AS quantidade_vendida
FROM vendas_novo vn
JOIN produtos p
    ON vn.produto_id = p.id
GROUP BY p.nome
ORDER BY quantidade_vendida DESC
LIMIT 5;

Pergunta:
Qual produto teve maior faturamento?

SQL:
SELECT
    p.nome,
    SUM(vn.valor) AS total_faturado
FROM vendas_novo vn
JOIN produtos p
    ON vn.produto_id = p.id
GROUP BY p.nome
ORDER BY total_faturado DESC
LIMIT 1;
"""
