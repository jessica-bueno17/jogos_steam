from typing import List, Dict, Any

def proporcao_avaliacoes_positivas(jogos: List[Dict], minimo_avaliacoes=20, top=5) -> List[Dict[str, Any]]:
    """
    Analisa a lista de jogos e encontra os 5 com a melhor proporção de avaliações positivas.
    
    Args:
        jogos (list): Uma lista de dicionários, onde cada dicionário é um jogo.
        minimo_avaliacoes (int): O número mínimo de avaliações para um jogo ser considerado.
        top (int): O número máximo de jogos na classificação.
        
    Returns:
        list: Uma lista de dicionários contendo o nome, preço, gênero e proporção dos 5 melhores jogos.
    """
    # Esta lista irá manter os 5 melhores jogos encontrados até o momento.
    top_jogos: List[Dict[str, Any]] = []

    for jogo in jogos:
        try:
            positivas = int(jogo['Positive'])
            negativas = int(jogo['Negative'])
            total_avaliacoes = positivas + negativas

            if total_avaliacoes >= minimo_avaliacoes:
                proporcao = positivas / total_avaliacoes
                
                # Dicionário com os dados do jogo atual
                jogo_atual_info = {
                    "nome": jogo['Name'],
                    "preco": float(jogo['Price']),
                    "proporcao": round(proporcao,2)
                }

                # Se a lista de top 5 ainda não está cheia, apenas adicionamos
                if len(top_jogos) < top:
                    top_jogos.append(jogo_atual_info)
                    # Mantém a lista ordenada da maior para a menor proporção
                    top_jogos.sort(key=lambda x: x['proporcao'], reverse=True)
                # Se a lista já está cheia, verificamos se o jogo atual é melhor que o pior da lista
                elif proporcao > top_jogos[-1]['proporcao']:
                    top_jogos.pop() # Remove o pior
                    top_jogos.append(jogo_atual_info) # Adiciona o novo
                    top_jogos.sort(key=lambda x: x['proporcao'], reverse=True) # Reordena

        except (ValueError, KeyError, ZeroDivisionError):
            # Ignora jogos com dados faltantes ou inválidos
            continue
            
    top_jogos = [
        {"nome": j["nome"], "preco": j["preco"], "proporcao": j["proporcao"]}
        for j in top_jogos
    ]

    exibir_tabela(top_jogos, f"🏆 Top {top} Jogos por Proporção de Avaliação Positiva 🏆")
            
    return top_jogos

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

