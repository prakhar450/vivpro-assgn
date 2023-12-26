from . import db
from sqlalchemy.dialects.postgresql import JSONB


class Song(db.Model):
    __tablename__ = 'playlist'

    song_id = db.Column(db.String(50), primary_key=True)
    song_title = db.Column(db.String(100), nullable=False)
    song_rating = db.Column(db.Float, nullable=True)  # Optional song rating
    dynamic_attrs = db.Column(JSONB)  # This column will store dynamic attributes as JSON

    def __repr__(self):
        return f"Post('{self.song_id}', '{self.song_title}')"
