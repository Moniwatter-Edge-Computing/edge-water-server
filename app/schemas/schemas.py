from pydantic import BaseModel, field_validator, model_validator
import json

class ConectaSchema(BaseModel):
    imei: str
    versao_fw: str

class EnviarConsumosSchema(BaseModel):
    fk_sistema: str

class EventoSchema(BaseModel):
    fk_sistema: int
    dataInicioEvento: str
    dataFimEvento: str
    nome: str
    id_firmware: int
    status: str

class EnviarEventosSchema(BaseModel):
    eventos: list[EventoSchema]


class EnviaStatusSchema(BaseModel):
    fk_sistema: int
    data_update: str

    entradasDigitais: list[int]
    ip_local: str
    saidasDigitais: list[int]
    EntradaAnalogica1: int
    EntradaAnalogica2: int
    nivelPrcTanqueInferior: int
    nivelPrcTanqueSuperior: int
    volumeNivelTanqueInferior: int
    volumeNivelTanqueSuperior: int
    tempoBomba1: float
    tempoBomba2: float
    tempoBomba3: float
    tempoBomba4: float
    hidrometro1: float
    hidrometro2: float
    vazaoLitroDiaH1: int
    vazaoLitroDiaH2: int

    @model_validator(mode="before")
    def flatten_status(cls, values):
        if "status" in values and isinstance(values["status"], dict):
            status_data = values.pop("status")
            values.update(status_data)

        return values

    @field_validator("entradasDigitais", "saidasDigitais", mode="before")
    def parse_list(cls, v):
        if isinstance(v, str):
            return json.loads(v)
        return v
