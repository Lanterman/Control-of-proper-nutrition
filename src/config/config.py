import os
import logging

from pathlib import Path


logging.basicConfig(
    format="[%(asctime)s] | %(levelname)s: %(message)s", 
    level=logging.INFO, 
    datefmt='%m.%d.%Y %H:%M:%S'
)

# Path
BASE_DIR = Path(__file__).resolve().parent.parent
PATH_TO_USER_DIRECTORIES = f"{BASE_DIR}/uploaded_photo"

DOMAIN = os.environ.get("DOC_DOMAIN", os.environ["DOMAIN"])

SECRET_KEY = os.environ.get("DOC_SECRET_KEY", os.environ["SECRET_KEY"])