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
    hourly: str = "",
    timezone: str = "America/Sao_Paulo"
):
    try:
        dados = carregar_dados_meteorologicos()
    except RuntimeError as erro:
        raise HTTPException(
            status_code=500,
            detail=str(erro)
        )

    if latitude != dados["latitude"] or longitude != dados["longitude"]:
        raise HTTPException(
            status_code=404,
            detail="Localidade não encontrada."
        )

    resposta = {
        "latitude": dados["latitude"],
        "longitude": dados["longitude"],
        "timezone": dados["timezone"],
        "timezone_abbreviation": dados["timezone_abbreviation"],
        "utc_offset_seconds": dados["utc_offset_seconds"],
        "elevation": dados["elevation"]
    }

    # Dados meteorológicos atuais
    if current:
        variaveis = current.split(",")

        resposta["current"] = {}
        resposta["current_units"] = {}

        for variavel in variaveis:
            if variavel not in dados["current"]:
                raise HTTPException(
                    status_code=400,
                    detail=f"Variável atual não disponível: {variavel}"
                )

            resposta["current"][variavel] = dados["current"][variavel]
            resposta["current_units"][variavel] = dados["current_units"][variavel]

        resposta["current"]["time"] = dados["current"]["time"]
        resposta["current_units"]["time"] = dados["current_units"]["time"]

    # Dados meteorológicos horários
    if hourly:
        variaveis = hourly.split(",")

        resposta["hourly"] = {}
        resposta["hourly_units"] = {}

        for variavel in variaveis:
            if variavel not in dados["hourly"]:
                raise HTTPException(
                    status_code=400,
                    detail=f"Variável horária não disponível: {variavel}"
                )

            resposta["hourly"][variavel] = dados["hourly"][variavel]
            resposta["hourly_units"][variavel] = dados["hourly_units"][variavel]

        resposta["hourly"]["time"] = dados["hourly"]["time"]
        resposta["hourly_units"]["time"] = dados["hourly_units"]["time"]

    return resposta
