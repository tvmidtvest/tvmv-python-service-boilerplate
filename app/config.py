import logging
import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

APP_PATH = os.path.dirname(os.path.abspath(__file__))

PARENT_PATH = Path(APP_PATH).parent
APP_PATH = Path(APP_PATH)

# Load environment variables from .env file
ENV_FILE = PARENT_PATH / '.env'

load_dotenv(ENV_FILE)

log_level = getattr(logging, os.environ['LOG_LEVEL'], logging.DEBUG)
log_to_console = os.environ['LOG_TO_CONSOLE'] == "true"

today = datetime.now().strftime("%Y-%m-%d")
log_filename = PARENT_PATH / f"logs/{today}.log"

handlers = [logging.FileHandler(log_filename)]

if log_to_console:
    handlers.append(logging.StreamHandler())

logging.basicConfig(
    level=log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=handlers
)


def get_logger(name: str):
    return logging.getLogger(name)
