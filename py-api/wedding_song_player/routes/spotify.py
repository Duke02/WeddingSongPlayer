import typing as tp

import fastapi
from fastapi import APIRouter
from spotipy import Spotify

from wedding_song_player.models.spotify import SongQueue, TrackObject, CurrentlyPlayingSongInfo, \
    CurrentlyPlayingTrack

spotify_router: APIRouter = APIRouter(prefix='/spotify', tags=['spotify', 'music'])

spotify_client: Spotify = Spotify()


@spotify_router.post('/pause', status_code=fastapi.status.HTTP_204_NO_CONTENT)
async def pause(device_id: str | None = None):
    spotify_client.pause_playback(device_id)


@spotify_router.post('/play', status_code=fastapi.status.HTTP_204_NO_CONTENT)
async def play(device_id: str | None = None):
    spotify_client.start_playback(device_id)


@spotify_router.get('/queue')
async def get_queue() -> SongQueue:
    queue: dict[tp.Literal['currently_playing', 'queue'], dict | list[dict]] = spotify_client.queue()
    currently_playing: TrackObject = TrackObject(**queue['currently_playing'])
    queue: list[TrackObject] = [TrackObject(**s) for s in queue['queue']]
    return SongQueue(currently_playing=currently_playing.to_song_info(), next_songs=[s.to_song_info() for s in queue])


@spotify_router.get('/current_song')
async def get_current_song() -> CurrentlyPlayingSongInfo | None:
    curr_track: CurrentlyPlayingTrack = CurrentlyPlayingTrack(**spotify_client.currently_playing())
    return curr_track.to_curr_playing_song_info()

