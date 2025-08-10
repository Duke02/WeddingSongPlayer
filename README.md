# Wedding Song Player

A song player that I hope to use for my wedding to my beautiful fiancé. I'm hoping to use this before the ceremony and possibly during the reception.

## Structure
- Rust Backend for fast AI inference
- Python API for querying Spotify/lyrics/etc APIs
- Angular front end for actually displaying the current song.

### Front-End Goals
- View of current song playing, including:
  - song name
  - album cover
  - artist name
  - song progress bar (how much time is left in the song, etc.)
  - genre?
- Lyrics of the current song, time-synced as best as possible
- (For songs not in English) automatic translation of songs (through Python and Rust API)
- Why a song was included for the playlist
- Who included the song 

### Stretch Front-End Goals
- Bio/Photo/etc of whoever is speaking (must be selectable from the website)
  - A super stretch goal could be automatically detecting it based on the mic, but eh. data privacy/etc concerns with that one.
- Store info into a SQL database so we don't have to query APIs a ton (in case the venue doesn't have good internet.)
- Display the song queue
