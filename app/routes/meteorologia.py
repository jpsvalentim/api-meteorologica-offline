from fastapi import APIRouter, HTTPException
from app.services import carregar_dados_meteorologicos

router = APIRouter()


@router.get("/health")
def verificar_status():
    return {
        "status": "online",
        "servico": "API Meteorológica Offline"
    }


@router.get("/v1/forecast")
def consultar_previsao(
    latitude: float,
    longitude: float,
    current: str = "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,wind_speed_10m",
    timezone: str = "America/Sao_Paulo"
):
    dados = carregar_dados_meteorologicos()

    if latitude != dados["latitude"] or longitude != dados["longitude"]:
        raise HTTPException(
            status_code=404,
            detail="Localidade não encontrada."
        )

    variaveis_disponiveis = dados["current"]

    variaveis_solicitadas = current.split(",")

    for variavel in variaveis_solicitadas:
        if variavel not in variaveis_disponiveis:
            raise HTTPException(
                status_code=400,
                detail=f"Variável não disponível: {variavel}"
            )

    resposta = {
        "latitude": dados["latitude"],
        "longitude": dados["longitude"],
        "timezone": dados["timezone"],
        "timezone_abbreviation": dados["timezone_abbreviation"],
        "utc_offset_seconds": dados["utc_offset_seconds"],
        "elevation": dados["elevation"],
        "current_units": {},
        "current": {}
    }

    for variavel in variaveis_solicitadas:
        resposta["current"][variavel] = variaveis_disponiveis[variavel]
        resposta["current_units"][variavel] = dados["current_units"][variavel]

    resposta["current"]["time"] = variaveis_disponiveis["time"]
    resposta["current_units"]["time"] = dados["current_units"]["time"]

    return resposta