from app.services.data_processorFor_api import status_data_processing, event_data_processing
from os import getenv
import requests
import json

def SendDataToAPI(route, data):
    API_URL = getenv("API_URL")
    if not API_URL:
        return "error: API_URL não configurada no .env"

    try:
        if route == "status":
            data_processed = status_data_processing(data)
        elif route == "events":
            data_processed = event_data_processing(data)
        else:
            # Caso haja a tentativa de envio em uma 3 rota ( so a duas na API atualmente)
            return print("Não foi possivel realizar o envio")
        
        response = requests.post(f"{API_URL}/hydric-ingest/{route}", json=data_processed)

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