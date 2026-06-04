SCHEMA = """
Banco PostgreSQL:

Tabela clientes:
id
nome
tipo_pessoa

Tabela produtos:
id
nome
preco

Tabela formas_pagamento:
id
descricao

Tabela vendas_novo:
id
cliente_id
produto_id
forma_pagamento_id
quantidade
valor
data_venda

Relacionamentos:
vendas_novo.cliente_id -> clientes.id
vendas_novo.produto_id -> produtos.id
vendas_novo.forma_pagamento_id -> formas_pagamento.id

Regras:
- Gere apenas SQL PostgreSQL
- Não explique
- Não use markdown
- Apenas SELECT
"""