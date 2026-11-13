from fastapi import FastAPI

app = FastAPI(
    title="API Meteorológica Offline",
    description="API local para disponibilização de dados meteorológicos.",
    version="1.0.0"
)


@app.get("/")
def inicio():
    return {
        "mensagem": "API Meteorológica Offline",
        "status": "online",
        "versao": "1.0.0"
    }