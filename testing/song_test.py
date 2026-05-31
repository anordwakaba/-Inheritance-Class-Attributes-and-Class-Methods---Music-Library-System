from lib.song import Song


def setup_function():
    Song.count = 0
    Song.genres = []
    Song.artists = []
    Song.genre_count = {}
    Song.artists_count = {}


def test_song_creation_increments_count():
    song = Song('Song One', 'Artist A', 'Pop')
    assert song.name == 'Song One'
    assert song.artist == 'Artist A'
    assert song.genre == 'Pop'
    assert Song.count == 1


def test_song_updates_unique_artists_and_genres():
    Song('Song Two', 'Artist B', 'Rock')
    Song('Song Three', 'Artist A', 'Pop')
    assert sorted(Song.artists) == ['Artist A', 'Artist B']
    assert sorted(Song.genres) == ['Pop', 'Rock']


def test_genre_and_artist_counts():
    Song('Song Four', 'Artist C', 'Jazz')
    Song('Song Five', 'Artist C', 'Jazz')
    Song('Song Six', 'Artist A', 'Pop')
    assert Song.genre_count['Jazz'] == 2
    assert Song.genre_count['Pop'] == 1
    assert Song.artists_count['Artist C'] == 2
    assert Song.artists_count['Artist A'] == 1


def test_no_duplicate_artists_or_genres():
    Song('Song Seven', 'Artist D', 'Hip-Hop')
    Song('Song Eight', 'Artist D', 'Hip-Hop')
    assert Song.artists.count('Artist D') == 1
    assert Song.genres.count('Hip-Hop') == 1
