import csv
import random

# Define os nomes dos arquivos e o tamanho da amostra
nome_arquivo_original = '../../steam_games.csv'
nome_arquivo_amostra = 'amostra_aleatoria_20_linhas.csv'
numero_de_linhas_amostra = 20

# Colunas que queremos manter
colunas_desejadas = ["Name", "Release date", "Price", "Genres", "Positive", "Negative"]

try:
    with open(nome_arquivo_original, 'r', newline='', encoding='utf-8') as f_in:
        leitor_csv = csv.reader(f_in)
        cabecalho = next(leitor_csv)

        # Pega os índices das colunas desejadas no cabeçalho original
        indices_colunas = [cabecalho.index(col) for col in colunas_desejadas]

        amostra = []
        for i, linha in enumerate(leitor_csv):
            if i < numero_de_linhas_amostra:
                amostra.append([linha[idx] for idx in indices_colunas])
            else:
                j = random.randint(0, i)
                if j < numero_de_linhas_amostra:
                    amostra[j] = [linha[idx] for idx in indices_colunas]

    with open(nome_arquivo_amostra, 'w', newline='', encoding='utf-8-sig') as f_out:
        # Muda delimitador para abrir no Excel
        escritor_csv = csv.writer(f_out, delimiter=';')
        
        # Escreve apenas as colunas desejadas
        escritor_csv.writerow(colunas_desejadas)
        escritor_csv.writerows(amostra)

    print(f"✅ Arquivo '{nome_arquivo_amostra}' foi gerado com sucesso!")

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo_original}' não foi encontrado. Verifique o caminho.")
except ValueError as ve:
    print(f"Erro: Alguma coluna desejada não foi encontrada no CSV. Detalhe: {ve}")
except StopIteration:
    print("Erro: O arquivo CSV parece estar vazio ou contém apenas a linha de cabeçalho.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")