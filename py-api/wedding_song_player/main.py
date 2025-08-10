"""
Wedding Song Player is an app that plays songs for my future wedding.

This Python portion of it is responsible for collecting Spotify information, as well
as lyrics and potentially whatever reason we decided to include a song.
"""
from dotenv import load_dotenv
from fastapi import FastAPI

from wedding_song_player.routes.spotify import spotify_router

load_dotenv()

app = FastAPI()

app.include_router(spotify_router)
