import os
import logging
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOGS_DIR, "app.log")


logging.basicConfig(
    filename= LOG_FILE,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level = logging.INFO,
)

logging.info("Configuration loaded successfully")