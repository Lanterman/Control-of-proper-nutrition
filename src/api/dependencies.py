from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends

# from services import auth as auth_service
from models import models as model


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> model.Users:
    """Authenticated user with jwt"""

    # user = await auth_service.get_user_by_token(token)
    # return user


# async def get_current_admin(token: str = Depends(oauth2_scheme)) -> users_model.Users:
#     """Authenticated admin with jwt"""

#     admin = await auth_service.get_admin_by_token(token)
#     return admin