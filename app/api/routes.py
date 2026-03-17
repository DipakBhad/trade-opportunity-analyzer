from fastapi import APIRouter, Request, Depends
from app.services.analysis_service import analyze_sector
from app.core.security import verify_api_key
from app.core.rate_limiter import limiter
from app.storage.session_store import add_request

router = APIRouter()

@router.get("/analyze/{sector}")
@limiter.limit("5/minute")
@router.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze(request: Request, sector: str, api_key: str = Depends(verify_api_key)):
    client_ip = request.client.host
    add_request(client_ip)

    return analyze_sector(sector)