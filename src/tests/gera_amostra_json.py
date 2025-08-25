import csv
import json

arquivo_csv = "amostra_aleatoria_20_linhas.csv"
arquivo_json = "amostra_aleatoria_20_linhas.json"

lista_de_jogos = []

# Lê o CSV e cria lista de dicionários
with open(arquivo_csv, mode="r", newline="", encoding="utf-8-sig") as file:
    leitor_csv = csv.DictReader(file, delimiter=";")  # 👈 corrigido
    lista_de_jogos = list(leitor_csv)

# Salva em arquivo JSON
with open(arquivo_json, mode="w", encoding="utf-8") as file:
    json.dump(lista_de_jogos, file, indent=4, ensure_ascii=False)

print("✅ Lista de dicionários criada e salva em JSON.")
