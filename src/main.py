
from utils.carrega_csv import carrega_csv
from utils.percentual_jogos_gratuitos import percentual_jogos_gratuitos
from utils.ano_mais_jogos import ano_mais_jogos
from utils.proporcao_avaliacoes_positivas import proporcao_avaliacoes_positivas

def app():

    jogos = carrega_csv('../steam_games.csv')

    percentual_jogos_gratuitos(jogos)
    print("*" * 40)

    ano_mais_jogos(jogos)
    print("*" * 40)

    proporcao_avaliacoes_positivas(jogos)
    print("*" * 40)

if __name__ == "__main__":
    app()

