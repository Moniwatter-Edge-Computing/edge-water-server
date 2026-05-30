class status_data_processing:
    def __init__(self, payload: dict):
        self.payload = payload

        processed_data = {
            "moni_id": str(self.payload["fk_sistema"]),
            "data_update": str(self.payload["data_update"]),

            "hidrometro1": float(self.payload["hidrometro1"]),
            "hidrometro2": float(self.payload["hidrometro1"]),

            "nivel_prc_tanque_inferior": int(self.payload["nivelPrcTanqueinferior"]),
            "nivel_prc_tanque_superior": int(self.payload["nivelPrcTanquesuperior"]),

            "tempo_bomba1": float(self.payload["tempoBomba1"]),
            "tempo_bomba2": float(self.payload["tempoBomba2"]),
            "tempo_bomba3": float(self.payload["tempoBomba3"]),
            "tempo_bomba4": float(self.payload["tempoBomba4"]),

            "vazao_litro_dia_h1": int(self.payload["vazaoLitroDiaH1"]),
            "vazao_litro_dia_h2": int(self.payload["vazaoLitroDiaH2"]),

            "volume_nivel_tanque_inferior": int(self.payload["volumeNivelTanqueInferior"]),
            "volume_nivel_tanque_superior":  int(self.payload["volumeNivelTanquesuperior"])
        }
        
        return processed_data