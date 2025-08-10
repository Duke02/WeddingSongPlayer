from dotenv import load_dotenv
from fastapi import FastAPI

from wedding_song_player.routes.spotify import spotify_router

load_dotenv()

app = FastAPI()

app.include_router(spotify_router)