from ..models import Song, db


def get_paginated_songs(page, per_page):
    try:
        return Song.query.paginate(page=page, per_page=per_page, error_out=False)
    except Exception as e:
        return None


def search_songs(search_term, page, per_page):
    try:
        song_query = Song.query.filter(Song.song_title.ilike(f'%{search_term}%'))
        return song_query.paginate(page=page, per_page=per_page, error_out=False)
    except Exception as e:
        return None


def update_song_rating(song_id, new_rating):
    try:
        song = Song.query.get(song_id)
        if song:
            song.star_rating = new_rating
            db.session.commit()
            return song
        else:
            return None
    except Exception as e:
        db.session.rollback()
        return None
