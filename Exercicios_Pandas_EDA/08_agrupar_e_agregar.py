"""Exercício 8: agrupar e agregar dados.

Explicação: Agrupamentos ajudam a resumir dados por categoria. Neste exercício,
você calcula totais e médias por categoria.

Pergunta: Qual é o valor total e a média de quantidade por categoria?
"""

import pandas as pd


def criar_df_vendas():
    return pd.DataFrame(
        {
            "produto": ["Caneta", "Caderno", "Mochila", "Caneta", "Borracha", "Caderno"],
            "categoria": ["Papelaria", "Papelaria", "Acessórios", "Papelaria", "Papelaria", "Papelaria"],
            "quantidade": [3, 2, 1, 5, 4, 1],
            "valor_total": [7.5, 24.0, 120.0, 12.5, 12.0, 12.0],
        }
    )


def agrupar_e_agregar(df_vendas: pd.DataFrame):
    print("=== Tabela de vendas ===")
    print(df_vendas, end="\n\n")

    total_por_categoria = df_vendas.groupby("categoria")["valor_total"].sum()
    media_quantidade = df_vendas.groupby("categoria")["quantidade"].mean()

    print("=== Valor total por categoria ===")
    print(total_por_categoria, end="\n\n")

    print("=== Média de quantidade por categoria ===")
    print(media_quantidade, end="\n\n")

    return total_por_categoria, media_quantidade


def rodar_exercicio():
    df_vendas = criar_df_vendas()
    total_por_categoria, media_quantidade = agrupar_e_agregar(df_vendas)
    assert total_por_categoria.loc["Papelaria"] == 55.5
    assert round(media_quantidade.loc["Papelaria"], 1) == 3.0


if __name__ == "__main__":
    rodar_exercicio()


# Explicação linha a linha
# 1-3: declara o objetivo e pergunta do exercício.
# 7-15: criamos o DataFrame com vendas e valores totais.
# 18-20: mostramos a tabela original.
# 22: somamos o valor_total por categoria.
# 23: calculamos a média de quantidade por categoria.
# 26-31: exibimos os resultados.
# 34-38: verificamos com asserts se os resultados estão corretos.
