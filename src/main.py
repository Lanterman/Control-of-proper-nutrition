import os
import uvicorn

from fastapi import FastAPI, status
from fastapi.openapi.utils import get_openapi

from db.db import TESTING
from config.utils import LockedError

from config.config import DOMAIN  # noqa
from models.models import Base
from api.auth import router as auth_router
from api.users import router as users_router
# from api.admin import router as admins_router
# from api.webhooks import router as webhooks_router

Base.metadata.create_all

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
# app.include_router(admins_router)
# app.include_router(webhooks_router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Healthy Body API",
        version="0.1.0",
        description="This is the Healthy Body OpenAPI schema!",
        routes=app.routes,
        contact={"GitHub": "https://github.com/Lanterman"}
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


if __name__ == "__main__":
    if TESTING:
        raise LockedError(
            status_code=status.HTTP_423_LOCKED,
            detail="To run the project, you need to set the TESTING variable to False"
        )

    uvicorn.run(
        app="main:app", reload=True, host=os.environ.get("DOC_HOST", os.environ["HOST"]),
        port=int(os.environ.get("DOC_PORT", os.environ["PORT"]))
    )
