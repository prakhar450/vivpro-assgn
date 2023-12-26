from playlist import create_app, db
import json
from playlist.models import Song
from sqlalchemy import inspect

def load_data():
    # Read and transform JSON
    with open('../data/playlist[76].json', 'r') as file:
        data = json.load(file)

    songs_data = {}
    for attr, songs in data.items():
        for song_id, value in songs.items():
            if song_id not in songs_data:
                songs_data[song_id] = {}
            songs_data[song_id][attr] = value
    songs_data = list(songs_data.values())

    # Process each song
    for song_data in songs_data:
        song_id = song_data.get('id', '0')
        song_title = song_data.get('title', 'Unknown Title')
        dynamic_attrs = {key: value for key, value in song_data.items() if key not in ['id', 'title']}

        # Create and add song
        song = Song(
            song_id=song_id,
            song_title=song_title,
            dynamic_attrs=dynamic_attrs
        )

        db.session.add(song)
        db.session.commit()


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        inspector = inspect(db.engine)
        if not inspector.has_table(Song.__tablename__):
            db.create_all()
            print(f"Table '{Song.__tablename__}' created.")
        else:
            print(f"Table '{Song.__tablename__}' already exists.")
        # Check if data needs to be loaded
        if not Song.query.first():
            load_data()
            print("Database initialized.")
        else:
            print("Database already initialized.")

