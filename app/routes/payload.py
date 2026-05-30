from app.schemas.schemas import ConectaSchema, EnviaStatusSchema, EnviarConsumosSchema, EnviarEventosSchema
from app.services.api_send import SendDataToAPI
from fastapi import APIRouter, Request
from datetime import datetime

router = APIRouter(tags=["rotas de conexão"])


@router.post("/conecta")
async def handshake(payload: ConectaSchema):
    currentDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # variavel com os dados validados abaixo
    data = payload.model_dump()

    

    return {
        "status": "OK",
        "mensagem": "",
        "codigo": 1,
        "token": "abc",
        "dataSistema": currentDate
    }

async def get_payload(request: Request):
    try:
        return await request.json()
    except Exception:
        return None

@router.put("/enviastatus")
async def envia_status(payload: EnviaStatusSchema):
    # variavel com os dados validados abaixo
    data = payload.model_dump()

    print("Resultado do envio para a API\n",SendDataToAPI("status", data))

    return {
        "status": "OK",
        "mensagem": "",
        "possuiNovaConfig": 0
    }


@router.post("/enviareventos")
async def enviar_eventos(payload: EnviarEventosSchema):

    # variavel com os dados validados abaixo
    data = payload.model_dump()

    eventos = data["eventos"]
    print("Resultado do envio para a API\n",SendDataToAPI("eventos", eventos))


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

    # variavel com os dados validados abaixo
    dados = payload.model_dump()

    return {
        "status": "OK",
        "mensagem": ""
    }