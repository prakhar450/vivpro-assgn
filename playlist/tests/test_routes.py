import json
from playlist.models import Song


def test_get_songs_route(test_client, init_database):
    response = test_client.get("/songs")
    assert response.status_code == 200
    # Check the response data
    data = json.loads(response.data)
    assert 'songs' in data
    assert 'total_pages' in data


def test_search_songs_route(test_client, init_database):
    response = test_client.get("/search?search=Test")
    assert response.status_code == 200
    # Check the response data
    data = json.loads(response.data)
    assert 'songs' in data
    assert 'total_pages' in data


def test_update_song_rating_route(test_client, init_database):
    song_id = "1"
    new_rating = 4.0
    response = test_client.put(f"/update_rating/{song_id}", json={"song_rating": new_rating})
    assert response.status_code == 200
    # Verify the response
    updated_song = Song.query.get(song_id)
    assert updated_song.song_rating == new_rating
