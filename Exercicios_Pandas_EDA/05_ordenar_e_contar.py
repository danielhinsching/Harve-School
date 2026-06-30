"""Exercício 5: ordenar e contar valores.

Explicação: Ordenação e contagem são operações comuns em EDA para identificar
os registros mais importantes e a frequência de cada valor.

Pergunta: Qual produto foi vendido mais vezes e qual é o pedido com maior valor total?
"""

import pandas as pd


def criar_df_vendas():
    return pd.DataFrame(
        {
            "pedido": [101, 102, 103, 104, 105, 106, 107],
            "produto": ["Caneta", "Caderno", "Mochila", "Caneta", "Borracha", "Caderno", "Caderno"],
            "quantidade": [3, 2, 1, 5, 4, 1, 2],
            "preco_unitario": [2.5, 12.0, 120.0, 2.5, 3.0, 12.0, 12.0],
        }
    )


def ordenar_e_contar(df_vendas: pd.DataFrame):
    print("=== Vendas originais ===")
    print(df_vendas, end="\n\n")

    df_vendas["valor_total"] = df_vendas["quantidade"] * df_vendas["preco_unitario"]
    vendas_ordenadas = df_vendas.sort_values(by="valor_total", ascending=False)
    print("=== Vendas ordenadas por valor total ===")
    print(vendas_ordenadas, end="\n\n")

    mais_vendido = df_vendas["produto"].value_counts()
    print("=== Contagem de vendas por produto ===")
    print(mais_vendido, end="\n\n")

    produto_top = mais_vendido.idxmax()
    print(f"Produto mais vendido: {produto_top}")
    print(f"Valor total do pedido mais alto: {vendas_ordenadas.iloc[0]['valor_total']}", end="\n\n")

    return produto_top, vendas_ordenadas.iloc[0]["valor_total"]


def rodar_exercicio():
    df_vendas = criar_df_vendas()
    produto_top, maior_valor = ordenar_e_contar(df_vendas)
    assert produto_top == "Caderno"
    assert maior_valor == 60.0


if __name__ == "__main__":
    rodar_exercicio()


# Explicação linha a linha
# 1-3: declaração do exercício e pergunta.
# 6-15: criamos um DataFrame de vendas com produto, quantidade e preço.
# 18-20: mostramos a tabela original de vendas.
# 22: calculamos o valor total para cada pedido.
# 23: ordenamos a tabela pelo valor total em ordem decrescente.
# 26-28: mostramos a tabela ordenada.
# 30: contamos quantas vezes cada produto aparece.
# 33-35: identificamos o produto mais vendido e o maior valor total.
# 38-43: a função principal roda o exercício e valida os resultados.
