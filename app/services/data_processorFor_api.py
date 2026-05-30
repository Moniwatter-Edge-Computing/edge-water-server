def status_data_processing(payload: dict):
    return {
        "moni_id": int(payload["fk_sistema"]),
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

def event_data_processing(payload_arr):

    # o pydantic está retornando um arr(eventos) contendo dentro um dict com todos os dados
    # por isso ele e acessado abaixo
    payload = payload_arr[0]

    return {
        "moni_id": int(payload["fk_sistema"]),

        "dataInicioEvento": str(payload["dataInicioEvento"]),
        "dataFimEvento": str(payload["dataFimEvento"]),

        "nome": str(payload["nome"]),
        "status": str(payload["status"]) 
    }