from typing import List, Dict, Any

def proporcao_avaliacoes_positivas(jogos: List[Dict], minimo_avaliacoes=20) -> List[Dict[str, Any]]:
    """
    Retorna todos os jogos gratuitos com 100% de avaliações positivas,
    considerando apenas jogos com um número mínimo de avaliações.
    
    Args:
        jogos (list): Lista de dicionários, onde cada dicionário é um jogo.
        minimo_avaliacoes (int): Número mínimo de avaliações para considerar o jogo.
        
    Returns:
        list: Lista de dicionários com nome, preço e proporção dos jogos gratuitos 100% positivos.
    """
    resultados: List[Dict[str, Any]] = []

    for jogo in jogos:
        try:
            preco = float(jogo['Price'])
            if preco != 0:  # Só considera jogos gratuitos
                continue

            positivas = int(jogo['Positive'])
            negativas = int(jogo['Negative'])
            total_avaliacoes = positivas + negativas

            if total_avaliacoes >= minimo_avaliacoes:
                proporcao = positivas / total_avaliacoes

                if proporcao == 1.0:  # Só considera proporção igual a 1
                    resultados.append({
                        "nome": jogo['Name'],
                        "preco": preco,
                        "proporcao": round(proporcao, 2)
                    })

        except (ValueError, KeyError, ZeroDivisionError):
            continue
            
    exibir_tabela(resultados, "🏆 Jogos Gratuitos com 100% de Avaliações Positivas 🏆")
    return resultados


def formatar_valor(key: str, value: Any) -> str:
    """Formata valores para exibição em tabela."""
    if isinstance(value, float):
        if key.lower() == "preco":
            return f"R${value:,.2f}"
        elif key.lower() == "proporcao":
            return f"{value:.2}"
    return str(value)


def exibir_tabela(dados: List[Dict[str, Any]], titulo: str) -> None:
    """Exibe os dados em formato tabular."""
    if not dados:
        print(f"--- {titulo} ---")
        print("Nenhum dado para exibir.")
        return

    cabecalhos = list(dados[0].keys())
    larguras_colunas = {key: len(key) for key in cabecalhos}

    for item in dados:
        for key, value in item.items():
            valor_formatado = formatar_valor(key, value)
            larguras_colunas[key] = max(larguras_colunas[key], len(valor_formatado))

    linha_cabecalho = " | ".join(key.ljust(larguras_colunas[key]) for key in cabecalhos)
    linha_separadora = "-|-".join("-" * larguras_colunas[key] for key in cabecalhos)

    print(f"--- {titulo} ---")
    print(linha_cabecalho)
    print(linha_separadora)

    for item in dados:
        celulas = [formatar_valor(key, item[key]).ljust(larguras_colunas[key]) for key in cabecalhos]
        print(" | ".join(celulas))

