import json
from utils.percentual_jogos_gratuitos import percentual_jogos_gratuitos

# Carrega a lista de dicionários json de amostra
with open("./tests/amostra_aleatoria_20_linhas.json", "r", encoding="utf-8") as f:
    jogos_amostra = json.load(f)

def teste_percentual_jogos_gratuitos():
    resultado = percentual_jogos_gratuitos(jogos_amostra)
    
    print("*** Iniciando teste: percentual_jogos_gratuitos ***")
    assert resultado["gratuito"] == 25
    assert resultado["pago"] == 75
    print("✅ Teste passou com sucesso!")

if __name__ == "__main__":
    teste_percentual_jogos_gratuitos()