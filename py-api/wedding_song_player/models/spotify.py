import typing as tp

from pydantic import BaseModel, Field


class ImageObject(BaseModel):
    url: str
    height: int | None
    width: int | None


class SongInfo(BaseModel):
    song_id: str
    title: str
    artists: list[str]
    album: str
    album_cover: ImageObject
    genres: list[str] = []


class SimplifiedArtistObject(BaseModel):
    external_urls: dict[str, str]
    href: str
    id: str
    name: str
    type: tp.Literal['artist'] = 'artist'
    url: str


class AlbumInfo(BaseModel):
    album_type: tp.Literal['album', 'single', 'compilation']
    total_tracks: int = Field(gt=0)
    available_markets: list[str]
    external_urls: dict[str, str]
    href: str
    id: str
    images: list[ImageObject]
    name: str
    release_date: str
    release_date_precision: tp.Literal['year', 'month', 'day']
    restrictions: dict[str, str]
    type: tp.Literal['album'] = 'album'
    url: str
    artists: list[SimplifiedArtistObject]


class TrackObject(BaseModel):
    """
    Direct class from Spotify's API.
    """
    album: AlbumInfo
    artists: list[SimplifiedArtistObject]
    available_markets: list[str]
    disc_number: int = Field(gt=0)
    duration_ms: int = Field(gt=0)
    explicit: bool
    external_ids: dict[str, str]
    external_urls: dict[str, str]
    href: str
    id: str
    is_playable: bool
    linked_from: dict
    restrictions: dict
    name: str
    popularity: int = Field(ge=0, le=100)
    preview_url: str | None = None
    track_number: int = Field(gt=0)
    type: tp.Literal['track'] = 'track'
    uri: str
    is_local: bool = False

    def to_song_info(self) -> SongInfo:
        return SongInfo(song_id=self.id, title=self.title, artists=[a.name for a in self.artists],
                        album=self.album.name, album_cover=self.album.images[0], genres=[])


class SongQueue(BaseModel):
    currently_playing: SongInfo
    next_songs: list[SongInfo]


class CurrentlyPlayingSongInfo(BaseModel):
    song_id: str
    song_length: float
    current_song_loc: float
    song_info: SongInfo


class Device(BaseModel):
    id: str | None = None
    is_active: bool = False
    is_private_session: bool = False
    is_restricted: bool = False
    name: str = ''
    type: str = ''
    volume_percent: int = Field(ge=0, le=100)
    supports_volume: bool = False


class Context(BaseModel):
    type: str
    href: str
    external_urls: dict[str, str]
    uri: str


class CurrentlyPlayingTrack(BaseModel):
    """
    Official Spotify class.
    https://developer.spotify.com/documentation/web-api/reference/get-the-users-currently-playing-track
    """
    device: Device
    repeat_state: tp.Literal['off', 'track', 'context']
    shuffle_state: bool
    context: Context | None = None
    timestamp: int = Field(ge=0)
    """
    Unix Millisecond Timestamp when playback state was last changed (play, pause, skip, scrub, new song, etc.).
    """
    progress_ms: int | None
    is_playing: bool
    item: TrackObject | None
    currently_playing_type: tp.Literal['track', 'episode', 'ad', 'unknown']
    actions: dict[str, bool] = {}

    def to_curr_playing_song_info(self) -> CurrentlyPlayingSongInfo | None:
        if self.item is None:
            return None
        return CurrentlyPlayingSongInfo(song_id=self.item.id, current_song_loc=self.progress_ms,
                                        song_length=self.item.duration_ms, song_info=self.item.to_song_info())
