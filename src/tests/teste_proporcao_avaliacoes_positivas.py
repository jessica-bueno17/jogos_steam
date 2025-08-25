import json
from utils.proporcao_avaliacoes_positivas import proporcao_avaliacoes_positivas

# Carrega a lista de dicionários json de amostra
with open("./tests/amostra_aleatoria_20_linhas.json", "r", encoding="utf-8") as f:
    jogos_amostra = json.load(f)


def teste_proporcao_avaliacoes_positivas():
    resultado = proporcao_avaliacoes_positivas(jogos_amostra)

    print("*** Iniciando teste: ano_mais_jogos ***")
    resultado_amostra = [
        {"nome": "Super Cucho", "preco": 1.99, "proporcao": 1},
        {"nome": "Mr.Hack Jack: Robot Detective", "preco": 14.99, "proporcao": 0.91},
        {"nome": "KINGDOM of the DEAD", "preco": 14.99, "proporcao": 0.83},
        {"nome": "Summer With You", "preco": 3.99, "proporcao": 0.76},
        {"nome": "Abstract Arena", "preco": 4.99, "proporcao": 0.55},
    ]
    assert resultado == resultado_amostra
    print("✅ Teste passou com sucesso!")


if __name__ == "__main__":
    teste_proporcao_avaliacoes_positivas()
