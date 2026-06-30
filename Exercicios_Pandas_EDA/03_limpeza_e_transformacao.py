"""Exercício 3: limpeza e transformação de dados.

Explicação: Este exercício corrige problemas comuns em uma tabela de pedidos,
como duplicatas, valores ausentes e formatos de data, e depois adiciona métricas.

Pergunta: Como deixar os dados prontos para análise e calcular o valor total por pedido?

A explicação linha a linha está no final do arquivo.
"""

import pandas as pd


def criar_df_com_erros():
    """Cria um DataFrame com duplicatas e valores ausentes."""
    return pd.DataFrame(
        {
            "pedido": [201, 202, 203, 203, 204, 205, 206],
            "cliente": ["Alice", "Bruno", "Carla", "Carla", "Diego", "Elisa", None],
            "produto": ["Caderno", "Caneta", "Caderno", "Caderno", "Mochila", "Borracha", "Caneta"],
            "categoria": ["Papelaria", "Papelaria", "Papelaria", "Papelaria", "Acessórios", "Papelaria", "Papelaria"],
            "quantidade": [1, 2, 2, 2, 1, None, 3],
            "preco_unitario": [15.0, 3.0, 15.0, 15.0, 120.0, 4.0, 3.0],
            "data_pedido": ["2026/06/01", "2026/06/01", "2026/06/02", "2026/06/02", "2026/06/03", "2026/06/04", "2026/06/04"],
        }
    )


def limpar_df(df: pd.DataFrame):
    """Remove duplicatas e trata valores ausentes."""
    print("=== Dados brutos ===")
    print(df, end="\n\n")

    df = df.drop_duplicates()
    print("Após remover duplicatas:")
    print(df, end="\n\n")

    df["cliente"] = df["cliente"].fillna("Não informado")
    df["quantidade"] = df["quantidade"].fillna(1).astype(int)

    df["data_pedido"] = pd.to_datetime(df["data_pedido"], format="%Y/%m/%d")
    df["produto"] = df["produto"].str.title()
    df["categoria"] = df["categoria"].str.capitalize()

    print("Após limpeza:")
    print(df, end="\n\n")

    return df


def criar_metrica_valor(df: pd.DataFrame):
    """Adiciona coluna de valor total e outras colunas úteis."""
    df["valor_total"] = df["quantidade"] * df["preco_unitario"]
    df["mes"] = df["data_pedido"].dt.month
    df["linha_completa"] = df["cliente"] != "Não informado"

    print("=== Dados com métricas ===")
    print(df[["pedido", "cliente", "valor_total", "mes", "linha_completa"]], end="\n\n")

    total_por_categoria = df.groupby("categoria")["valor_total"].sum()
    print("Valor total por categoria:")
    print(total_por_categoria, end="\n\n")

    return df


def rodar_exercicio():
    df = criar_df_com_erros()
    df_limpo = limpar_df(df)
    df_final = criar_metrica_valor(df_limpo)

    assert df_final["quantidade"].isna().sum() == 0
    assert df_final["valor_total"].min() >= 3.0
    assert df_final["data_pedido"].dtype == "datetime64[ns]"


if __name__ == "__main__":
    rodar_exercicio()


# Explicação linha a linha
# 1-3: importamos pandas para manipular o DataFrame.
# 7-19: criamos uma tabela com pedidos contendo duplicatas e valores faltantes.
# 22-39: removemos duplicatas, substituímos clientes faltantes e convertimos quantidade para inteiro.
# 41-48: convertemos a coluna de data e padronizamos nomes de produto e categoria.
# 51-58: adicionamos uma coluna de valor total e extraímos o mês de pedido.
# 59: criamos uma coluna booleana para indicar se a linha tem cliente informado.
# 61-66: mostramos as métricas e o valor total por categoria.
# 69-77: executamos o exercício e verificamos as transformações com asserts.
