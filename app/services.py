import json
from pathlib import Path


CAMINHO_DADOS = Path(__file__).parent / "data" / "dados_meteorologicos.json"


def carregar_dados_meteorologicos():
    try:
        with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return dados

    except FileNotFoundError:
        raise RuntimeError("Arquivo de dados meteorológicos não encontrado.")

    except json.JSONDecodeError:
        raise RuntimeError("O arquivo JSON possui um formato inválido.")