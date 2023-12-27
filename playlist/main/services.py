from ..models import Song, db


def get_paginated_songs(page, per_page):
    """
    Fetches songs from the database in a paginated format.

    Parameters:
    - page (int): Page number for pagination.
    - per_page (int): Number of items per page.

    Returns:
    - Pagination object containing songs and pagination details.
    - None if an exception occurs.
    """
    try:
        return Song.query.paginate(page=page, per_page=per_page, error_out=False)
    except Exception as e:
        return None


def search_songs(search_term, page, per_page):
    """
    Searches and fetches songs based on a search term with pagination.

    Parameters:
    - search_term (str): Term used to filter songs by title.
    - page (int): Page number for pagination.
    - per_page (int): Number of items per page.

    Returns:
    - Pagination object containing filtered songs and pagination details.
    - None if an exception occurs.
    """
    try:
        song_query = Song.query.filter(Song.song_title.ilike(f'%{search_term}%'))
        return song_query.paginate(page=page, per_page=per_page, error_out=False)
    except Exception as e:
        return None


def update_song_rating(song_id, new_rating):
    """
    Updates the star rating of a specific song.

    Parameters:
    - song_id (str): The unique identifier of the song.
    - new_rating (float/int): New rating to be set for the song.

    Returns:
    - Song object with updated rating.
    - None if the song is not found or an exception occurs.
    """
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
