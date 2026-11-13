# API Meteorológica Offline

API REST desenvolvida com **Python e FastAPI** para disponibilização de dados meteorológicos simulados, armazenados localmente em JSON.

O projeto foi desenvolvido para permitir o consumo de informações meteorológicas por aplicações Python, sem necessidade de conexão com serviços externos.

## 1. Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- JSON
- Requests (para aplicações consumidoras)

## 2. Estrutura do projeto

```text
api-meteorologica-offline/
├── app/
│   ├── data/
│   │   └── dados_meteorologicos.json
│   ├── routes/
│   │   ├── __init__.py
│   │   └── meteorologia.py
│   ├── __init__.py
│   ├── main.py
│   └── services.py
├── .gitignore
├── requirements.txt
└── README.md
```

## 3. Instalação

### Pré-requisitos

- Python 3.10 ou superior.
- pip.

### Clonar o repositório

```bash
git clone https://github.com/jpsvalentim/api-meteorologica-offline.git
```

Acessar a pasta:

```bash
cd api-meteorologica-offline
```

### Criar ambiente virtual

Windows PowerShell:

```powershell
python -m venv .venv
```

Ativar o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

## 4. Executar a API

Com o ambiente virtual ativado, execute:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

Documentação interativa Swagger:

```text
http://127.0.0.1:8000/docs
```

## 5. Endpoints disponíveis

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Informações gerais da API |
| GET | `/health` | Verificação de disponibilidade |
| GET | `/v1/forecast` | Consulta de dados meteorológicos |

## 6. Consulta meteorológica

O endpoint `/v1/forecast` disponibiliza informações meteorológicas atuais e horárias.

### Parâmetros

| Parâmetro | Tipo | Descrição |
|---|---|---|
| latitude | float | Latitude da localidade |
| longitude | float | Longitude da localidade |
| current | string | Variáveis meteorológicas atuais desejadas |
| hourly | string | Variáveis meteorológicas horárias desejadas |
| forecast_days | integer | Limite de dias utilizado no cálculo dos registros horários |
| timezone | string | Fuso horário informado na consulta |

Localidade disponível:

- Latitude: `-26.4851`
- Longitude: `-49.0713`
- Fuso horário: `America/Sao_Paulo`

### Variáveis atuais disponíveis

- `temperature_2m`
- `relative_humidity_2m`
- `apparent_temperature`
- `precipitation`
- `wind_speed_10m`

### Variáveis horárias disponíveis

- `temperature_2m`
- `relative_humidity_2m`
- `precipitation`
- `wind_speed_10m`

## 7. Exemplos de requisição

### Consultar dados atuais

```text
http://127.0.0.1:8000/v1/forecast?latitude=-26.4851&longitude=-49.0713
```

### Consultar dados horários

```text
http://127.0.0.1:8000/v1/forecast?latitude=-26.4851&longitude=-49.0713&current=&hourly=temperature_2m,precipitation
```

### Consultar dados atuais e horários

```text
http://127.0.0.1:8000/v1/forecast?latitude=-26.4851&longitude=-49.0713&current=temperature_2m,relative_humidity_2m&hourly=temperature_2m,precipitation&forecast_days=1
```

## 8. Exemplo de consumo com Python Requests

```python
import requests

url = "http://127.0.0.1:8000/v1/forecast"

params = {
    "latitude": -26.4851,
    "longitude": -49.0713,
    "current": "temperature_2m,relative_humidity_2m",
    "hourly": "temperature_2m,precipitation",
    "forecast_days": 1
}

resposta = requests.get(url, params=params)

if resposta.status_code == 200:
    dados = resposta.json()
    print(dados)
else:
    print("Erro:", resposta.status_code, resposta.text)
```

## 9. Códigos de resposta

| Código HTTP | Significado |
|---|---|
| 200 | Consulta realizada com sucesso |
| 400 | Parâmetro ou variável inválida |
| 404 | Localidade não encontrada |
| 422 | Erro de validação dos parâmetros |
| 500 | Erro interno relacionado ao processamento dos dados |

## 10. Observações

- Os dados meteorológicos são simulados e armazenados localmente em JSON.
- A API não realiza consultas a serviços meteorológicos externos.
- A localidade disponível é Jaraguá do Sul – SC.
- A quantidade de registros horários retornados depende dos dados existentes no arquivo JSON.
- O parâmetro `forecast_days` estabelece um limite de registros, não gera novos dados meteorológicos.
- A estrutura das respostas é inspirada na Open-Meteo, sem implementar integralmente sua API.

---

**API Meteorológica Offline — Projeto desenvolvido para integração e consumo de dados por aplicações Python.**