from sse_starlette.sse import EventSourceResponse
from fastapi import APIRouter, Request
from routers.status_event_generator import *
import uvicorn


router = APIRouter()

@router.get('/stream')
async def runStatus(
        param1: str,
        request: Request
):
    event_generator = status_event_generator(request, param1)
    return EventSourceResponse(event_generator)
