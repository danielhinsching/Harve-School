"""Exercício 6: trabalhar com datas.

Explicação: Datas são um tipo especial de dado. Neste exercício, você aprende a
converter strings para datas e a extrair partes como mês e dia.

Pergunta: Quantos pedidos foram feitos em junho de 2026 e quais dias tiveram mais pedidos?
"""

import pandas as pd


def criar_df_pedidos():
    return pd.DataFrame(
        {
            "pedido": [201, 202, 203, 204, 205, 206, 207],
            "data_pedido": ["2026-06-01", "2026-06-01", "2026-06-02", "2026-06-02", "2026-06-03", "2026-06-03", "2026-07-01"],
            "valor": [50.0, 30.0, 20.0, 40.0, 60.0, 20.0, 80.0],
        }
    )


def analisar_datas(df_pedidos: pd.DataFrame):
    print("=== Pedidos originais ===")
    print(df_pedidos, end="\n\n")

    df_pedidos["data_pedido"] = pd.to_datetime(df_pedidos["data_pedido"])
    df_pedidos["mes"] = df_pedidos["data_pedido"].dt.month
    df_pedidos["dia"] = df_pedidos["data_pedido"].dt.day

    pedidos_junho = df_pedidos[df_pedidos["mes"] == 6]
    print("=== Pedidos em junho de 2026 ===")
    print(pedidos_junho, end="\n\n")

    mais_pedidos_por_dia = pedidos_junho["dia"].value_counts().sort_index()
    print("=== Contagem de pedidos por dia em junho ===")
    print(mais_pedidos_por_dia, end="\n\n")

    return pedidos_junho, mais_pedidos_por_dia


def rodar_exercicio():
    df_pedidos = criar_df_pedidos()
    pedidos_junho, mais_pedidos_por_dia = analisar_datas(df_pedidos)
    assert len(pedidos_junho) == 6
    assert mais_pedidos_por_dia.idxmax() == 1


if __name__ == "__main__":
    rodar_exercicio()


# Explicação linha a linha
# 1-3: descrição do exercício e pergunta.
# 7-15: criamos um DataFrame de pedidos com datas em formato string.
# 18-20: exibimos a tabela original.
# 22: convertemos a coluna de data para datetime.
# 23-24: extraímos mês e dia em novas colunas.
# 26-29: filtramos apenas pedidos de junho de 2026.
# 31-34: contamos quantos pedidos aconteceram em cada dia de junho.
# 37-39: função principal que executa o exercício.
