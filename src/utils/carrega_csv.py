import csv
from typing import List

def carrega_csv(file) -> List:
    """
    Carrega os dados de um arquivo CSV e os retorna como uma lista de dicionários.
    Cada dicionário representa um jogo.

    Args:
        file: O caminho para o arquivo CSV.
    """
    try:
        with open(file, 'r', encoding='utf-8') as arquivo_csv:

            leitor_csv = csv.DictReader(arquivo_csv)
            # Monta uma lista de dicionários com cada linha do arquivo
            lista_de_jogos = list(leitor_csv)

        return lista_de_jogos
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file}' não foi encontrado.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")