from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def verificar_status():
    return {
        "status": "online",
        "servico": "API Meteorológica Offline"
    }