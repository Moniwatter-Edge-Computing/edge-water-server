from fastapi import Request
from user_agents import parse
from os import getenv
import httpx
import asyncio


LOGVIEW_URL = getenv("LOGVIEW_URL")


def request_info(request: Request) -> dict:
    ua = parse(request.headers.get("User-Agent", ""))

    return {
        "IP": request.headers.get(
            "X-Forwarded-For",
            request.client.host
        ).split(",")[0].strip(),
        "Port": request.client.port,
        "Browser": f"{ua.browser.family} {ua.browser.version_string}",
        "OS": f"{ua.os.family} {ua.os.version_string}",
        "Device": ua.device.family,
        "method": request.method,
        "endpoint": request.url.path
    }


async def _send(payload: dict):
    if not LOGVIEW_URL:
        print("LOGVIEW_URL não configurada")
        return

    async with httpx.AsyncClient() as client:
        await client.post(LOGVIEW_URL, json=payload)


def dispatch_error(request: Request, message: str = "error"):
    payload = {
        "status": "NOK",
        "message": message,
        **request_info(request)
    }

    asyncio.create_task(_send(payload))


def dispatch_success(request: Request, data: dict = None):
    payload = {
        "status": "OK",
        **(data or {}),
        **request_info(request)
    }

    asyncio.create_task(_send(payload))