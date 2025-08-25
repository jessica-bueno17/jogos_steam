import json
from utils.ano_mais_jogos import ano_mais_jogos

# Carrega a lista de dicionários json de amostra
with open("./tests/amostra_aleatoria_20_linhas.json", "r", encoding="utf-8") as f:
    jogos_amostra = json.load(f)

def teste_ano_mais_jogos():
    resultado = ano_mais_jogos(jogos_amostra)

    print("*** Iniciando teste: ano_mais_jogos ***")
    assert resultado[0]["ano"] == "2022"
    print("✅ Teste passou com sucesso!")

if __name__ == "__main__":
    teste_ano_mais_jogos()
