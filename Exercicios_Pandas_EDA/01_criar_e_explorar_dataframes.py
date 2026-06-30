"""Exercício 1: criar e explorar DataFrames.

Explicação: Este exercício mostra como montar DataFrames simples em pandas e realizar
consultas básicas, como ver o início dos dados, os tipos de coluna e estatísticas.

Pergunta: Construa três DataFrames de exemplo e responda:
1. Quais são os três primeiros alunos?
2. Qual é o valor total de cada venda?
3. Qual cidade teve a maior temperatura média?

Cada bloco também traz uma explicação linha a linha no final.
"""

import pandas as pd


def criar_df_alunos():
    """Cria um DataFrame de alunos."""
    return pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "nome": ["Ana", "Bruno", "Carla", "Diego", "Elisa"],
            "idade": [18, 19, 18, 20, 19],
            "turma": ["A", "A", "B", "B", "A"],
            "nota_final": [8.5, 7.0, 9.2, 6.8, 8.0],
            "presenca": [92, 88, 100, 70, 95],
        }
    )


def criar_df_vendas():
    """Cria um DataFrame de vendas."""
    return pd.DataFrame(
        {
            "pedido": [101, 102, 103, 104, 105, 106],
            "produto": ["Caneta", "Caderno", "Mochila", "Caneta", "Borracha", "Caderno"],
            "categoria": ["Papelaria", "Papelaria", "Acessórios", "Papelaria", "Papelaria", "Papelaria"],
            "quantidade": [3, 2, 1, 5, 4, 1],
            "preco_unitario": [2.5, 12.0, 120.0, 2.5, 3.0, 12.0],
        }
    )


def criar_df_tempo():
    """Cria um DataFrame de temperatura."""
    return pd.DataFrame(
        {
            "data": ["2026-06-01", "2026-06-01", "2026-06-02", "2026-06-02", "2026-06-03"],
            "cidade": ["São Paulo", "Rio de Janeiro", "São Paulo", "Curitiba", "Rio de Janeiro"],
            "temperatura": [22.5, 26.0, 24.0, 18.0, 27.3],
            "chuva_mm": [1.2, 0.0, 5.4, 10.1, 0.0],
            "vento_kmh": [15, 10, 12, 25, 8],
        }
    )


def explorar_df_alunos(df_alunos: pd.DataFrame):
    print("=== Exemplo de alunos ===")
    print(df_alunos.head(), end="\n\n")

    print("Tipos de dados por coluna:")
    print(df_alunos.dtypes, end="\n\n")

    print("Notas e presença dos alunos:")
    print(df_alunos[["nome", "nota_final", "presenca"]], end="\n\n")


def explorar_df_vendas(df_vendas: pd.DataFrame):
    print("=== Exemplo de vendas ===")
    print(df_vendas.head(), end="\n\n")

    df_vendas["valor_total"] = df_vendas["quantidade"] * df_vendas["preco_unitario"]
    print("Valor total de cada venda:")
    print(df_vendas[["pedido", "produto", "valor_total"]], end="\n\n")


def explorar_df_tempo(df_tempo: pd.DataFrame):
    print("=== Exemplo de tempo ===")
    print(df_tempo.head(), end="\n\n")

    df_tempo["data"] = pd.to_datetime(df_tempo["data"])
    media_por_cidade = df_tempo.groupby("cidade")["temperatura"].mean()
    print("Temperatura média por cidade:")
    print(media_por_cidade, end="\n\n")


def rodar_exercicio():
    df_alunos = criar_df_alunos()
    df_vendas = criar_df_vendas()
    df_tempo = criar_df_tempo()

    explorar_df_alunos(df_alunos)
    explorar_df_vendas(df_vendas)
    explorar_df_tempo(df_tempo)


if __name__ == "__main__":
    rodar_exercicio()


# Explicação linha a linha
# 1-3: importamos pandas como pd para criar e manipular DataFrames.
# 7-17: construir um DataFrame de alunos usando um dicionário de listas.
# 20-30: criar um DataFrame de vendas com colunas de pedido, produto, categoria, quantidade e preço.
# 33-43: criar um DataFrame de tempo com data, cidade, temperatura, chuva e vento.
# 46-50: exibir as primeiras linhas do DataFrame de alunos.
# 52-54: exibir os tipos de cada coluna no DataFrame de alunos.
# 56-58: exibir somente as colunas de nome, nota_final e presença.
# 61-65: exibir as primeiras linhas do DataFrame de vendas.
# 67: calcular o valor total por linha multiplicando quantidade por preço unitário.
# 68-70: exibir as vendas com o valor total calculado.
# 73-77: exibir as primeiras linhas do DataFrame de tempo.
# 79: converter a coluna data para o tipo datetime.
# 80-82: agrupar por cidade e calcular a média de temperatura.
# 86-94: executar todas as funções quando o arquivo é chamado diretamente.
