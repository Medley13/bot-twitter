import tweepy
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
API_KEY = os.getenv("AG5RhI0Cunza7BbZFJaydIsrWK")
API_SECRET = os.getenv("Um3CDHeNki64oeeaUNP59ECSxYnWZFR6m9gzP8t9u2cqKyPrEy")
ACCESS_TOKEN = os.getenv("1823714527575465991-cKpgWFQHc5zZ2oQnA2devzDqnaM6l6")
ACCESS_TOKEN_SECRET = os.getenv("4foEG2ycBOmDp8eRmOOcwMzfusytuW54v1LurzhPE50sf")

# Authentification avec Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Créer une instance de l'API Tweepy
api = tweepy.API(auth)

# Exemple d'envoi d'un tweet
api.update_status("Hello, Twitter! Ce tweet est envoyé par un bot.")
