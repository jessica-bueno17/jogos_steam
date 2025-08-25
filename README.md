# Análise de Jogos Steam

Este projeto realiza uma análise básica de jogos da Steam a partir de um arquivo CSV.  
Ele calcula estatísticas como:

- Ano com mais lançamentos de jogos
- Percentual de jogos gratuitos e pagos
- Jogos com melhor proporção de avaliações positivas

### Arquivo CSV

O arquivo `steam_games.csv` já está incluído no repositório, dentro do diretório raiz.  
Não é necessário baixar ou mover nada; todas as funções e testes já estão configurados para utilizá-lo.

## Funções principais

- ano_mais_jogos(jogos) → Retorna o(s) ano(s) com mais lançamentos.
- percentual_jogos_gratuitos(jogos) → Retorna o percentual de jogos gratuitos e pagos.
- proporcao_avaliacoes_positivas(jogos) → Retorna os top 5 jogos por proporção de avaliações positivas.
- carrega_csv(caminho_arquivo) → Carrega um CSV e retorna uma lista de dicionários.

## Testes
Para a realização dos testes foram gerados arquivos csv e JSON com amostras aleatórias de 20 jogos.
Os testes devem ser executados no seguinte diretório `/src`. Execute o comando abaixo no terminal:

```bash
python -m tests.<nome_do_teste>
```

Obs.: Substitua <nome_do_teste> pelo nome do arquivo de teste, sem a extensão .py.

### Amostras geradas

O repositório contém em `src/tests/`  dois scripts que foram usados para gerar arquivos de amostra a partir do CSV original:

- `gera_amostra_csv.py` → gera uma amostra CSV com 20 jogos  
- `gera_amostra_json.py` → gera uma amostra JSON com 20 jogos  

**Observação:** os arquivos de amostra (`amostra_aleatoria_20_linhas.csv` e `amostra_aleatoria_20_linhas.json`) já foram gerados e estão incluídos no repositório.  
Não é necessário executar esses scripts novamente.  

Todos os testes foram executados com base nesses arquivos de amostra.

Além disso, existe o arquivo `analise_amostra.csv`, que foi utilizado apenas para análise exploratória dos dados e validação dos valores. Ele não é necessário para executar as funções ou os testes.

## Dependências

- Python 3.x
- Bibliotecas padrão: csv, json, random, collections

## Observações

- O projeto usa Python puro, sem frameworks de teste externos.
- Os testes são feitos com assert e mensagens simples no console.


