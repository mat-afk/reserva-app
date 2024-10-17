from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST: str = os.getenv("DB_HOST")
DB_USER: str = os.getenv("DB_USER")
DB_PASSWORD: str = os.getenv("DB_PASSWORD")
DB_NAME: str = os.getenv("DB_NAME")

if not DB_HOST:
    DB_HOST = "localhost"

if not DB_USER:
    DB_USER = "estudante1"

if not DB_PASSWORD:
    DB_PASSWORD = "estudante1"

if not DB_NAME:
    DB_NAME = "reserva_app"