import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY not found! Please set it in .env file.")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


