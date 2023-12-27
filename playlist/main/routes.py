from flask import Blueprint, request, jsonify
from .services import get_paginated_songs, search_songs, update_song_rating

application = Blueprint('application', __name__)


@application.route("/")
@application.route("/songs")
def get_songs():
    """
    GET endpoint to fetch paginated songs.
    Returns a list of songs with pagination details.

    Query Parameters:
    - page (int): The page number for pagination. Defaults to 1.
    - per_page (int): The number of items per page. Defaults to 5.

    Returns:
    - On Success: JSON object containing 'songs' and 'total_pages'.
    - On Failure: JSON object with 'error' message and a 500 status code.
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    paginated_songs = get_paginated_songs(page, per_page)

    if paginated_songs is None:
        return jsonify({'error': 'Failed to fetch songs'}), 500

    songs = [song.to_dict() for song in paginated_songs.items]
    return jsonify({'songs': songs, 'total_pages': paginated_songs.pages})


@application.route("/search")
def search_songs_route():
    """
    GET endpoint for searching songs based on the title.
    Supports pagination.

    Query Parameters:
    - search (str): The search term for filtering songs by title.
    - page (int): The page number for pagination. Defaults to 1.
    - per_page (int): The number of items per page. Defaults to 5.

    Returns:
    - On Success: JSON object containing 'songs' and 'total_pages'.
    - On Failure: JSON object with 'error' message and a 500 status code.
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    search_term = request.args.get('search', '', type=str)
    paginated_songs = search_songs(search_term, page, per_page)

    if paginated_songs is None:
        return jsonify({'error': 'Failed to search songs'}), 500

    songs = [song.to_dict() for song in paginated_songs.items]
    return jsonify({'songs': songs, 'total_pages': paginated_songs.pages})


@application.route('/update_rating/<song_id>', methods=['POST'])
def update_song_rating_route(song_id):
    """
    POST endpoint to update the star rating of a song.

    URL Parameters:
    - song_id (str): The unique identifier of the song.

    JSON Payload:
    - song_rating (float/int): The new star rating to be set for the song.

    Returns:
    - On Success: JSON object with 'message' indicating successful update.
    - On Failure: JSON object with 'error' message and appropriate status code.
    """
    data = request.get_json()
    if 'song_rating' not in data or not isinstance(data['song_rating'], (float, int)):
        return jsonify({'error': 'Invalid or missing star_rating'}), 400

    song = update_song_rating(song_id, data['song_rating'])
    if song is None:
        return jsonify({'error': 'Failed to update song rating or song not found'}), 500

    return jsonify({'message': 'Rating updated successfully'}), 200


if __name__ == '__main__':
    application.run(debug=True)


