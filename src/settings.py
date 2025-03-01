from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI", "postgresql://admin:admin@127.0.0.1/curotec")