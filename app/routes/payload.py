from app.schemas.schemas import ConectaSchema, EnviaStatusSchema, EnviarConsumosSchema, EnviarEventosSchema
from app.data_processing.status_processor import status_data_processing
from fastapi import APIRouter, Request
from datetime import datetime
from os import getenv
import requests
import json

router = APIRouter(tags=["rotas de conexão"])

def SendDataToAPI(data):
    API_URL = getenv("API_URL_TEST")

    if not API_URL:
        return "error: API_URL_TEST não configurada no .env"

    try:
        response = requests.post(API_URL, json=data)

        status = response.status_code

        try:
            content = json.dumps(response.json(), indent=4, ensure_ascii=False)
        except Exception:
            content = response.text

        if status != 200:
            return f"error: {content}"

        return f"success: {content}"

    except Exception as e:
        return f"error: {str(e)}"

@router.post("/conecta")
async def handshake(payload: ConectaSchema):
    data_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    dados = payload.model_dump()

    print("Resultado do envio para a API\n",SendDataToAPI(dados))

    return {
        "status": "OK",
        "mensagem": "",
        "codigo": 1,
        "token": "abc",
        "dataSistema": data_str
    }

async def get_payload(request: Request):
    try:
        return await request.json()
    except Exception:
        return None

@router.put("/enviastatus")
async def envia_status(payload: EnviaStatusSchema):
    dados = payload.model_dump()

    print("Resultado do envio para a API\n",SendDataToAPI(dados))

    return {
        "status": "OK",
        "mensagem": "",
        "possuiNovaConfig": 0
    }


@router.post("/enviareventos")
async def enviar_eventos(payload: EnviarEventosSchema):
    dados = payload.model_dump()

    eventos = dados["eventos"]

    print("Eventos recebidos:")
    print(eventos)

    return {
        "result": [
            {
                "status": "OK",
                "mensagem": "",
                "id": 0
            }
        ]
    }


@router.put("/enviaconfig1")
async def enviar_config1(request: Request):
    payload = await get_payload(request)

    if not payload:
        print("ERRO, Payload não foi recebido em /enviaconfig1")
        return {
            "status": "NOK",
            "mensagem": ""
        }

    print(f"Payload recebido em /enviaconfig1: \n{payload}")

    return {
        "status": "OK",
        "mensagem": ""
    }


@router.post("/enviarconsumos")
async def enviar_consumos(payload: EnviarConsumosSchema):
    dados = payload.model_dump()

    print("Resultado do envio para a API\n",SendDataToAPI(dados))

    return {
        "status": "OK",
        "mensagem": ""
    }