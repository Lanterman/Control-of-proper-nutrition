import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

# To run the project, you need to set the TESTING variable to False.
# To run the tests, you need to set the TESTING variable to True.
TESTING = False

DATABASE_URL = os.environ.get("DOC_DATABASE_URL", os.environ["DATABASE_URL"])

TESTING_DATABASE_URL = os.environ.get("DOC_TESTING_DATABASE_URL", os.environ["TESTING_DATABASE_URL"])

if TESTING:
    engine = create_async_engine(TESTING_DATABASE_URL, echo=True)
else:
    engine = create_async_engine(DATABASE_URL, echo=True)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)