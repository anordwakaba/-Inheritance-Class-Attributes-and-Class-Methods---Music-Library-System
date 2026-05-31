# Music Library System

This repository contains a `Song` class used to model songs in a music library.

## Song Class Features

- Instance attributes:
  - `name`
  - `artist`
  - `genre`
- Class attributes:
  - `count` — total number of songs created
  - `genres` — list of unique genres
  - `artists` — list of unique artists
  - `genre_count` — counts of songs per genre
  - `artists_count` — counts of songs per artist

## Usage

```python
from lib.song import Song
song = Song('Hello', 'Adele', 'Pop')
print(Song.count)
print(Song.artists)
print(Song.genre_count)
```

## Running tests

```bash
pip install pytest
pytest -q
```
