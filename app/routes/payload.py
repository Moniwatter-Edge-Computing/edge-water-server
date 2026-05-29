from app.schemas.enviarconsumos import enviarconsumosSchema
from app.schemas.enviareventos import enviareventosSchema
from app.schemas.enviastatus import enviastatusSchema
from app.schemas.conecta import conectaSchema
from fastapi import APIRouter, Request
from datetime import datetime

router = APIRouter(tags=["rotas de conexão"])

@router.post("/conecta")
async def handshake(request: Request, payload: conectaSchema):
    data_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    dados = payload.model_dump()

    print(f"Payload recebido em /conecta:\n{dados}")

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
async def envia_status(request: Request):
    payload = await get_payload(request)

    if not payload:
        print("ERRO, Payload não foi recebido em /enviastatus")
        return {
            "status": "OK",
            "mensagem": "",
            "possuiNovaConfig": 0
        }

    print(f"Payload recebido em /enviastatus: \n{payload}")

    return {
        "status": "OK",
        "mensagem": "",
        "possuiNovaConfig": 0
    }


@router.post("/enviareventos")
async def enviar_eventos(request: Request):
    payload = await get_payload(request)

    if not payload:
        print("ERRO, Payload não foi recebido em /enviareventos")
        return {
            "result": [
                {
                    "status": "NOK",
                    "mensagem": "",
                    "id": 0
                }
            ]
        }

    print(f"Payload recebido em /enviareventos: \n{payload}")

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
async def enviar_consumos(request: Request):
    payload = await get_payload(request)

    if not payload:
        print("ERRO, Payload não foi recebido em /enviarconsumos")
        return {
            "status": "NOK",
            "mensagem": ""
        }

    print(f"Payload recebido em /enviarconsumos: \n{payload}")

    return {
        "status": "OK",
        "mensagem": ""
    }