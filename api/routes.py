from fastapi import APIRouter, HTTPException
from services.email_analyzer import analyze_email
from schemas.request_schema import EmailRequest
from schemas.response_schema import EmailResponse

router = APIRouter()

@router.post("/analyze", response_model=EmailResponse)
def analyze(data: EmailRequest):
    try:
        result = analyze_email(data.email)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error during email analysis")
