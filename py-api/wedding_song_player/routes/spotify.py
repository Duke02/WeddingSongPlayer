"""
The actual API definitions of our Spotify uses.
"""
import typing as tp

import fastapi
from fastapi import APIRouter
from spotipy import Spotify

from wedding_song_player.models.spotify import SongQueue, TrackObject, \
    CurrentlyPlayingSongInfo, CurrentlyPlayingTrack

spotify_router: APIRouter = APIRouter(prefix='/spotify', tags=['spotify', 'music'])

spotify_client: Spotify = Spotify()


# pylint: disable=unused-variable
@spotify_router.post('/pause', status_code=fastapi.status.HTTP_204_NO_CONTENT)
async def pause(device_id: str | None = None):
    """
    Pauses the currently playing song.
    :param device_id: The optional ID of the device to pause.
    :return: A 204 status code, nothing else.
    """
    spotify_client.pause_playback(device_id)


# pylint: disable=unused-variable
@spotify_router.post('/play', status_code=fastapi.status.HTTP_204_NO_CONTENT)
async def play(device_id: str | None = None):
    """
    Resumes the currently playing song.
    :param device_id: The ID of the device to play on.
    :return: Nothing except for a 204 status code.
    """
    spotify_client.start_playback(device_id)


# pylint: disable=unused-variable
@spotify_router.get('/queue')
async def get_queue() -> SongQueue:
    """
    Gets the queue of the current user.
    :return: The queue of the current user.
    """
    queue: dict[tp.Literal['currently_playing', 'queue'], dict | list[
        dict]] = spotify_client.queue()
    currently_playing: TrackObject = TrackObject(**queue['currently_playing'])
    queue: list[TrackObject] = [TrackObject(**s) for s in queue['queue']]
    return SongQueue(currently_playing=currently_playing.to_song_info(),
                     next_songs=[s.to_song_info() for s in queue])


# pylint: disable=unused-variable
@spotify_router.get('/current_song')
async def get_current_song() -> CurrentlyPlayingSongInfo | None:
    """
    Gets the currently playing song of the user.
    :return: The currently playing song if available, None otherwise.
    """
    curr_track: CurrentlyPlayingTrack = CurrentlyPlayingTrack(
        **spotify_client.currently_playing())
    return curr_track.to_curr_playing_song_info()
