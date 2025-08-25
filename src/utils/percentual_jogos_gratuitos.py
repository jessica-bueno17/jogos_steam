from typing import List, Dict

def percentual_jogos_gratuitos(jogos: List[Dict]) ->  dict[str, float]:
    """ Calcula o percentual de jogos gratuitos e pagos em uma lista de jogos.

    Percorre a lista de jogos, verifica o preço de cada um e calcula 
    a porcentagem de jogos gratuitos (preço 0) e pagos (preço maior que 0).

    Args:
        jogos (List[Dict]): Lista de dicionários, onde cada item deve conter 
            a chave 'Price' representando o preço do jogo (pode ser string ou float).

    Returns:
        Dict[str, float]: Dicionário com duas chaves:
            - 'gratuito': percentual de jogos gratuitos (float, 2 casas decimais).
            - 'pago': percentual de jogos pagos (float, 2 casas decimais).
    """
    if not jogos:
        return {"gratuito": 0.0, "pago": 0.0}

    jogos_pagos = 0
    jogos_gratuitos = 0

    for jogo in jogos:
        try:
            preco = float(jogo["Price"])

        except (ValueError, TypeError, KeyError):
            continue  # ignora entradas inválidas

        if preco == 0:
            jogos_gratuitos +=1
        else:
            jogos_pagos +=1

    numero_jogos = jogos_pagos + jogos_gratuitos

    percentual_gratuitos = round((jogos_gratuitos / numero_jogos) * 100, 2)
    percentual_pagos = round((jogos_pagos / numero_jogos) * 100, 2)
    
    resultado = {"gratuito": percentual_gratuitos, "pago": percentual_pagos}
    
    exibir_percentual(resultado)

    return resultado

def exibir_percentual(resultados: Dict[str, float]) -> None:
    """Exibe no console os percentuais de jogos gratuitos e pagos."""
    print("📊 Percentual de Jogos")
    print(f"💸 Gratuitos: {resultados['gratuito']:>6.2f}%")
    print(f"💰 Pagos   : {resultados['pago']:>6.2f}%")