import json
from pathlib import Path


CAMINHO_DADOS = Path(__file__).parent / "data" / "dados_meteorologicos.json"


def carregar_dados_meteorologicos():
    with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados