from flask import Blueprint, request, jsonify
from playlist.models import Song

application = Blueprint('application', __name__)


@application.route("/")
@application.route("/home")
def home():
    page = request.args.get('page', 1, type=int)  # Default to page 1
    per_page = request.args.get('per_page', 5, type=int)  # Default 5 items per page

    paginated_songs = Song.query.paginate(page=page, per_page=per_page, error_out=False)
    songs = paginated_songs.items

    return jsonify([song.song_title for song in songs])


if __name__ == '__main__':
    application.run(debug=True)
