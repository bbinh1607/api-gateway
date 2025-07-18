from dotenv import load_dotenv
import os

dotenv_path=os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config:
    API_PREFIX = os.getenv("API_PREFIX")
    DEVICE_SERVICE_URL = os.getenv("DEVICE_SERVICE_URL")
    IDENTITY_SERVICE_URL = os.getenv("IDENTITY_SERVICE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    PERMANENT_SESSION_LIFETIME = int(os.getenv("PERMANENT_SESSION_LIFETIME", 30))