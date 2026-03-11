import os
from dotenv import load_dotenv

load_dotenv()

# Application configuration
class settings:
    PROJECT_NAME ='Car Price API'
    API_KEY = os.getenv('API_KEY', 'demo_key')  # Default to 'demo_key' if not set
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'secret')
    JWT_ALGORITHM = 'HS256'
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
    MODEL_PATH='app/models/model.pkl'

settings = settings() 
