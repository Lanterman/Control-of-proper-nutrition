from fastapi import Depends, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm

# from services import auth as auth_service
from schemas import auth as auth_schema


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("", 
             response_model=auth_schema.BaseToken, 
             status_code=status.HTTP_202_ACCEPTED,
             responses={400: {"description": "Incorrect email or password!"}})
async def auth(form_data: OAuth2PasswordRequestForm = Depends()):
    """User authenticated - endpoint"""

    # token = await auth_service.auth(form_data)
    # return token
