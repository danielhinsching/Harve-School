"""Exercício 7: identificar e tratar valores ausentes.

Explicação: Dados reais frequentemente têm valores faltantes. Este exercício
mostra como localizar esses valores e como preenchê-los com valores padrão.

Pergunta: Quantas linhas têm valores ausentes e como podemos preencher esses valores
com um valor padrão?
"""

import pandas as pd


def criar_df_com_ausentes():
    return pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "produto": ["Caneta", "Caderno", None, "Mochila", "Borracha"],
            "quantidade": [3, None, 2, 1, 4],
            "categoria": ["Papelaria", "Papelaria", "Papelaria", None, "Papelaria"],
        }
    )


def tratar_ausentes(df: pd.DataFrame):
    print("=== Dados com valores ausentes ===")
    print(df, end="\n\n")

    faltantes_por_coluna = df.isna().sum()
    print("=== Contagem de valores ausentes por coluna ===")
    print(faltantes_por_coluna, end="\n\n")

    df["produto"] = df["produto"].fillna("Desconhecido")
    df["quantidade"] = df["quantidade"].fillna(1).astype(int)
    df["categoria"] = df["categoria"].fillna("Papelaria")

    print("=== Dados após preencher valores ausentes ===")
    print(df, end="\n\n")

    return df


def rodar_exercicio():
    df = criar_df_com_ausentes()
    df_tratado = tratar_ausentes(df)
    assert df_tratado.isna().sum().sum() == 0


if __name__ == "__main__":
    rodar_exercicio()


# Explicação linha a linha
# 1-3: declara o objetivo e a pergunta do exercício.
# 7-15: criamos um DataFrame com valores ausentes em produto, quantidade e categoria.
# 18-20: mostramos a tabela original com os dados ausentes.
# 22: contamos quantos valores ausentes existem em cada coluna.
# 25-27: preenchermos os valores ausentes com valores padrão.
# 29-31: mostramos a tabela após o tratamento.
# 34-37: função principal que valida que não há mais valores ausentes.
