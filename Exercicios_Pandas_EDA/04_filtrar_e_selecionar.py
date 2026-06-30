"""Exercício 4: filtrar e selecionar dados.

Explicação: Este exercício mostra como usar filtros em pandas para encontrar
apenas os registros que atendem a uma condição, e como selecionar apenas algumas colunas.

Pergunta: Quais alunos da turma A têm nota final maior ou igual a 8.0?
"""

import pandas as pd


def criar_df_alunos():
    return pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5, 6],
            "nome": ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Fabio"],
            "idade": [18, 19, 18, 20, 19, 21],
            "turma": ["A", "A", "B", "B", "A", "A"],
            "nota_final": [8.5, 7.0, 9.2, 6.8, 8.0, 8.7],
        }
    )


def filtrar_alunos(df_alunos: pd.DataFrame):
    print("=== Lista original de alunos ===")
    print(df_alunos, end="\n\n")

    alunos_turma_a = df_alunos[(df_alunos["turma"] == "A") & (df_alunos["nota_final"] >= 8.0)]
    print("=== Alunos da turma A com nota >= 8.0 ===")
    print(alunos_turma_a, end="\n\n")

    alunos_selecionados = alunos_turma_a[["nome", "nota_final"]]
    print("=== Nome e nota dos alunos selecionados ===")
    print(alunos_selecionados, end="\n\n")

    return alunos_selecionados


def rodar_exercicio():
    df_alunos = criar_df_alunos()
    result = filtrar_alunos(df_alunos)
    assert not result.empty


if __name__ == "__main__":
    rodar_exercicio()


# Explicação linha a linha
# 1-3: declaração do exercício com objetivo e pergunta.
# 5: importamos pandas para trabalhar com DataFrames.
# 9-18: construímos o DataFrame de alunos com informações de turma e nota.
# 21-23: mostramos a tabela completa de alunos.
# 25: criamos um filtro para escolher apenas alunos da turma A com nota >= 8.0.
# 26-28: exibimos o resultado do filtro.
# 30: selecionamos apenas as colunas nome e nota_final para simplificar a visualização.
# 33-35: exibimos a tabela final com os campos pedidos.
# 38-40: função principal que roda o exercício e garante que há resultado.
