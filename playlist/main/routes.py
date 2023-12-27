from flask import Blueprint, request, jsonify
from services import get_paginated_songs, search_songs, update_song_rating

application = Blueprint('application', __name__)


@application.route("/")
@application.route("/songs")
def get_songs():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    paginated_songs = get_paginated_songs(page, per_page)

    if paginated_songs is None:
        return jsonify({'error': 'Failed to fetch songs'}), 500

    songs = [song.to_dict() for song in paginated_songs.items]
    return jsonify({'songs': songs, 'total_pages': paginated_songs.pages})


@application.route("/search")
def search_songs_route():
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
    data = request.get_json()
    if 'star_rating' not in data or not isinstance(data['star_rating'], (float, int)):
        return jsonify({'error': 'Invalid or missing star_rating'}), 400

    song = update_song_rating(song_id, data['star_rating'])
    if song is None:
        return jsonify({'error': 'Failed to update song rating or song not found'}), 500

    return jsonify({'message': 'Rating updated successfully'}), 200


if __name__ == '__main__':
    application.run(debug=True)


