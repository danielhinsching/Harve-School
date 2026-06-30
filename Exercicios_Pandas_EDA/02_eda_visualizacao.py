"""Exercício 2: EDA e visualização de dados.

Explicação: Este exercício mostra como transformar dados numéricos e gerar
visualizações simples a partir de um DataFrame de vendas.

Pergunta: Quantos produtos foram vendidos em cada categoria e como isso aparece
em um gráfico de barras?

As explicações linha a linha aparecem no final do arquivo.
"""

import pandas as pd
import matplotlib.pyplot as plt


def criar_df_vendas():
    """Cria um DataFrame com dados de venda fictícios."""
    return pd.DataFrame(
        {
            "produto": ["Xadrez", "Caderno", "Caneta", "Caderno", "Mochila", "Xadrez", "Borracha"],
            "categoria": ["Jogos", "Papelaria", "Papelaria", "Papelaria", "Acessórios", "Jogos", "Papelaria"],
            "quantidade": [2, 3, 5, 1, 1, 1, 4],
            "preco_unitario": [80.0, 15.0, 3.0, 15.0, 120.0, 80.0, 4.0],
            "data": ["2026-06-01", "2026-06-01", "2026-06-02", "2026-06-02", "2026-06-03", "2026-06-03", "2026-06-04"],
        }
    )


def calcular_valor_total(df_vendas: pd.DataFrame):
    """Adiciona uma coluna com o valor total de cada linha."""
    df_vendas["valor_total"] = df_vendas["quantidade"] * df_vendas["preco_unitario"]
    return df_vendas


def analisar_vendas(df_vendas: pd.DataFrame):
    """Realiza análise básica de vendas e mostra os resultados."""
    print("=== Vendas ===")
    print(df_vendas.head(), end="\n\n")

    print("Resumo numérico:")
    print(df_vendas.describe(), end="\n\n")

    print("Contagem por categoria:")
    print(df_vendas["categoria"].value_counts(), end="\n\n")

    vendas_por_categoria = df_vendas.groupby("categoria")["valor_total"].sum().sort_values(ascending=False)
    print("Valor total por categoria:")
    print(vendas_por_categoria, end="\n\n")

    return df_vendas, vendas_por_categoria


def gerar_graficos(df_vendas: pd.DataFrame, vendas_por_categoria: pd.Series):
    """Gera e salva dois gráficos como imagens PNG."""
    plt.figure(figsize=(8, 4))
    vendas_por_categoria.plot(kind="bar", color=["#4C72B0", "#55A868", "#C44E52"])
    plt.title("Vendas por categoria")
    plt.ylabel("Valor total")
    plt.tight_layout()
    plt.savefig("vendas_por_categoria.png")
    print("Gráfico de vendas por categoria salvo em vendas_por_categoria.png")

    plt.figure(figsize=(8, 4))
    df_vendas["valor_total"].plot(kind="hist", bins=5, color="#8172B2")
    plt.title("Distribuição de valor total por pedido")
    plt.xlabel("Valor total")
    plt.tight_layout()
    plt.savefig("distribuicao_valor_total.png")
    print("Histograma salvo em distribuicao_valor_total.png")


def rodar_exercicio():
    df_vendas = criar_df_vendas()
    df_vendas = calcular_valor_total(df_vendas)
    df_vendas, vendas_por_categoria = analisar_vendas(df_vendas)
    gerar_graficos(df_vendas, vendas_por_categoria)


if __name__ == "__main__":
    rodar_exercicio()


# Explicação linha a linha
# 1-4: importamos pandas para manipular dados e matplotlib para gráficos.
# 8-18: criamos o DataFrame de vendas com produto, categoria, quantidade e preço.
# 21-23: função que calcula o valor total por linha e adiciona à tabela.
# 26-40: função de análise que mostra o DataFrame, resumo numérico e vendas por categoria.
# 43-61: função de visualização que cria um gráfico de barras e um histograma e salva como PNG.
# 64-69: função principal que executa todas as etapas.
