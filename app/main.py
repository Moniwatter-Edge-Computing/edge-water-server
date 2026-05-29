from app.logs.logs_dispatch import dispatch_success, dispatch_error
from fastapi import FastAPI, Request
from app.routes import payload, conection_routes
from dotenv import load_dotenv
from os import getenv

load_dotenv()

IS_PROD = getenv("ENV") == "production"

app = FastAPI(
    title="Telemetry API",
    docs_url=None if IS_PROD else "/docs",
    redoc_url=None if IS_PROD else "/redoc",
    openapi_url=None if IS_PROD else "/openapi.json"
)

@app.middleware("http")
async def log_all_requests(request: Request, call_next):
    try:
        response = await call_next(request)

        dispatch_success(request, {
            "status_code": response.status_code
        })

        return response

    except Exception as e:
        dispatch_error(request, str(e))

        raise

@app.get("/")
def health():
    return {"status": "online"}

app.include_router(payload.router)
app.include_router(conection_routes.router)