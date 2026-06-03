import random
import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Carregar variáveis de ambiente
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Criar conexão
engine = create_engine(DATABASE_URL)

print("Conectando ao banco...")

with engine.connect() as conn:

    # Buscar clientes
    clientes = [
        row[0]
        for row in conn.execute(
            text("SELECT id FROM clientes")
        ).fetchall()
    ]

    # Buscar produtos
    produtos = conn.execute(
        text("""
            SELECT id, preco
            FROM produtos
        """)
    ).fetchall()

    # Buscar formas de pagamento
    formas_pagamento = [
        row[0]
        for row in conn.execute(
            text("SELECT id FROM formas_pagamento")
        ).fetchall()
    ]

    print(f"Clientes encontrados: {len(clientes)}")
    print(f"Produtos encontrados: {len(produtos)}")
    print(f"Formas de pagamento encontradas: {len(formas_pagamento)}")

    # Gerar 500 vendas
    for _ in range(500):

        cliente_id = random.choice(clientes)

        produto_id, preco = random.choice(produtos)

        forma_pagamento_id = random.choice(formas_pagamento)

        quantidade = random.randint(1, 10)

        valor = float(preco) * quantidade

        dias = random.randint(0, 365)

        data_venda = datetime.now() - timedelta(days=dias)

        conn.execute(
            text("""
                INSERT INTO vendas_novo (
                    cliente_id,
                    produto_id,
                    forma_pagamento_id,
                    quantidade,
                    valor,
                    data_venda
                )
                VALUES (
                    :cliente_id,
                    :produto_id,
                    :forma_pagamento_id,
                    :quantidade,
                    :valor,
                    :data_venda
                )
            """),
            {
                "cliente_id": cliente_id,
                "produto_id": produto_id,
                "forma_pagamento_id": forma_pagamento_id,
                "quantidade": quantidade,
                "valor": valor,
                "data_venda": data_venda
            }
        )

    conn.commit()

print("500 vendas geradas com sucesso!")