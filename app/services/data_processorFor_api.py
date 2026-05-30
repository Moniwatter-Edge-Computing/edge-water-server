def status_data_processing(payload: dict):
    return {
        "moni_id": str(payload["fk_sistema"]),
        "data_update": str(payload["data_update"]),

        "hidrometro1": float(payload["hidrometro1"]),
        "hidrometro2": float(payload["hidrometro2"]),

        "nivel_prc_tanque_inferior": int(payload["nivelPrcTanqueInferior"]),
        "nivel_prc_tanque_superior": int(payload["nivelPrcTanqueSuperior"]),

        "tempo_bomba1": float(payload["tempoBomba1"]),
        "tempo_bomba2": float(payload["tempoBomba2"]),
        "tempo_bomba3": float(payload["tempoBomba3"]),
        "tempo_bomba4": float(payload["tempoBomba4"]),

        "vazao_litro_dia_h1": int(payload["vazaoLitroDiaH1"]),
        "vazao_litro_dia_h2": int(payload["vazaoLitroDiaH2"]),

        "volume_nivel_tanque_inferior": int(payload["volumeNivelTanqueInferior"]),
        "volume_nivel_tanque_superior": int(payload["volumeNivelTanqueSuperior"])
    }

def event_data_processing(payload: dict):
    return {
        "moni_id": int["fk_sistema"],

        "dataInicioEvento": "dataInicioEvento",
        "dataFimEvento": str(payload["dataFimEvento"]),

        "nome": str(payload["nome"]),
        "status": str(payload["status"]) 
    }