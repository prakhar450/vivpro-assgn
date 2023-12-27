import pytest
from .. import create_app, db
from ..config import TestConfig
from ..models import Song


@pytest.fixture(scope='function')
def test_client():
    app = create_app(TestConfig)
    testing_client = app.test_client()

    with app.app_context():
        db.create_all()
        yield testing_client
        db.session.remove()


@pytest.fixture(scope='function')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert sample data
    song1 = Song(song_id="1", song_title="Test Song 1", song_rating=4.5, dynamic_attrs={"genre": "Pop"})
    song2 = Song(song_id="2", song_title="Test Song 2", song_rating=3.5, dynamic_attrs={"genre": "Rock"})
    db.session.add(song1)
    db.session.add(song2)
    db.session.commit()

    yield db  # Testing happens here

    db.session.delete(song1)
    db.session.delete(song2)
    db.session.commit()
