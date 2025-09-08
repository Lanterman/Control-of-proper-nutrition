from fastapi import Depends, APIRouter, status

from .dependencies import get_current_user
# from services import users as users_service
# from schemas import users as users_schema
from models.models import Users


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/profile", 
            # response_model=users_schema.ProfileUserSchema, 
            status_code=status.HTTP_200_OK,
            responses={404: {"description": "No such user!"},
                       401: {"description": "Invalid authentication credentials"}})
async def get_user_profile(current_user: Users = Depends(get_current_user)):
    """Get user info - endpoint"""

    # user_info = await users_service.get_user_info(current_user.id)
    # return user_info