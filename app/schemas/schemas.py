from pydantic import BaseModel, field_validator
import json


class conectaSchema(BaseModel):
    imei: str
    versao_fw: str

class enviarconsumosSchema(BaseModel):
    fk_sistema: str

    
class enviareventosSchema(BaseModel):
    print("em desenvolvimento")

class enviastatusSchema(BaseModel):
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

    @field_validator("entradasDigitais", "saidasDigitais", mode="before")
    def parse_list(cls, v):
        if isinstance(v, str):
            return json.loads(v)
        return v