from flask import Blueprint, request, jsonify
from playlist.models import Song

application = Blueprint('application', __name__)


@application.route("/")
@application.route("/home")
def home():
    page = request.args.get('page', 1, type=int)  # Default to page 1
    per_page = request.args.get('per_page', 5, type=int)  # Default 5 items per page
    search = request.args.get('search', '', type=str)
    song_query = Song.query
    if search:
        song_query = song_query.filter(Song.title.ilike(f'%{search}%'))
    paginated_songs = song_query.paginate(page=page, per_page=per_page, error_out=False)
    songs = [song.to_dict() for song in paginated_songs.items]
    return jsonify({'songs': songs, 'total_pages': paginated_songs.pages})


if __name__ == '__main__':
    application.run(debug=True)
