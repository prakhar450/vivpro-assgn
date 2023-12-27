from ..main.services import get_paginated_songs, search_songs, update_song_rating


def test_get_paginated_songs(test_client, init_database):
    # Assume default pagination settings
    page = 1
    per_page = 5
    result = get_paginated_songs(page, per_page)
    assert result is not None
    assert len(result.items) <= per_page


def test_search_songs(test_client, init_database):
    search_term = "Test"
    page = 1
    per_page = 5
    result = search_songs(search_term, page, per_page)
    assert result is not None


def test_update_song_rating(test_client, init_database):
    # Assuming a song with id "1" exists in the test data
    new_rating = 4.0
    song_id = "1"
    result = update_song_rating(song_id, new_rating)
    assert result is not None
    assert result.song_rating == new_rating
