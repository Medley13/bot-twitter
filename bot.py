import os
from dotenv import load_dotenv

# Charger les variables depuis le fichier .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

print(f"Clé API : {API_KEY}")  # Vérifiez si les clés sont chargées