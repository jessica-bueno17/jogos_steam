from typing import List, Dict

def ano_mais_jogos(jogos: List[Dict]) -> List[Dict]:
    """
    Calcula e retorna o(s) ano(s) com o maior número de lançamentos de jogos.

    Utiliza a função `ano_jogos` para contar os jogos por ano e identifica 
    o(s) ano(s) que tiveram a maior quantidade. Se houver empate, retorna 
    todos os anos empatados.

    Args:
        jogos (List[Dict]): Lista de dicionários, onde cada item deve conter 
        a chave "Release date" no formato de string (ex.: "Oct 21, 2008").

    Returns:
        List[Dict]: Uma lista de dicionários, onde cada um contém as
        chaves 'ano' e 'quantidade'. A lista é ordenada crescentemente
        pelo ano e pode conter múltiplos itens em caso de empate.
    """
    contagem = ano_jogos(jogos)

    if not contagem:
        return []

    # maior quantidade de jogos
    max_qtd = max(contagem.values())

    # pega todos os anos que têm essa quantidade
    anos_max = [
        {"ano": ano, "quantidade": qtd}
        for ano, qtd in contagem.items()
        if qtd == max_qtd
    ]

    # ordenar os anos em ordem crescente
    anos_max.sort(key=lambda x: x["ano"])

    exibir_resultado(anos_max)

    return anos_max

def ano_jogos(jogos: List[Dict]) -> Dict[str, int]:
    """Conta quantos jogos existem por ano.

    Percorre a lista de jogos, extrai o ano do campo "Release date" 
    e soma a quantidade de jogos lançados em cada ano.

    Args:
        jogos (List[Dict]): Lista de dicionários, onde cada item deve conter 
        a chave "Release date" no formato de string (ex.: "Oct 21, 2008").

    Returns:
        Dict[str, int]: Dicionário onde a chave é o ano (string) e o valor é a 
        quantidade de jogos lançados naquele ano.
    """
    anos_jogos: Dict[str, int] = {}

    for jogo in jogos:
        data = jogo["Release date"]
        
        try:
            # pega os últimos 4 caracteres (o ano)
            ano = data[-4:] 
        except (ValueError, IndexError):
            continue  # ignora registros inválidos

        # incrementa ou inicia em 1
        anos_jogos[ano] = anos_jogos.get(ano, 0) + 1

    return anos_jogos

def exibir_resultado(anos: List[Dict]) -> None:
    """Exibe uma tabela formatada dos anos com mais lançamentos de jogos.

    Esta função recebe uma lista de dicionários, onde cada um representa um
    ano e a quantidade de jogos correspondente. A saída é uma tabela de texto
    impressa diretamente no console, ideal para visualização de resultados de
    uma análise.

    Args:
        anos (List[Dict]): Uma lista de dicionários. Cada dicionário
        deve conter as chaves 'ano' e 'quantidade', representando um ano e o 
        número de jogos lançados nele.

    Returns:
        None: A função não retorna nenhum valor, seu único efeito é imprimir
        no console.
    """
    print("📈 Ano(os) com mais jogos lançados:")
    print("Ano".ljust(10), "Jogos".rjust(10))
    print("-" * 20)
    for item in anos:
        print(item["ano"].ljust(10), str(item["quantidade"]).rjust(10))
        