# Vivpro Take Home Assignment

This project is a music playlist application using Flask and PostgreSQL. It allows users to view songs, search for songs, and update song ratings.

## Prerequisites

- Python 3
- pip (Python package manager)
- PostgreSQL
- Postman (optional, for API testing)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Clone the Repository

```bash
git clone https://github.com/prakhar450/vivpro-assgn.git
cd vivpro-assgn
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Database Setup

1. Install PostgreSQL.
2. Create two databases named `flask_db` and `test_db`.
3. Run the database initialization script:

   ```bash
   python initialize_database.py
   ```

   This will create a table called 'playlist' in `flask_db` with 100 songs.

### Running the Application

To start the server:

```bash
python run.py
```

Now, the Flask server is running and can serve requests.

## Testing the API

You can test the API endpoints using tools like Postman or `curl`.

- **Get All Songs**: `GET /songs`
- **Search for Songs**: `GET /search?search=Car` (Replace 'Car' with your search query)
- **Update Song Rating**: `POST /update_rating/<song_id>` with JSON payload `{"song_rating": 4.0}`

## Running Tests

To run automated tests for this system:

```bash
pytest
```

## Screenshots

Below are screenshots demonstrating the API functionality:

**Get All Songs**  
![Get All Songs](https://github.com/prakhar450/vivpro-assgn/assets/55326021/21b99b66-72b0-4e8d-8a5e-55d8b3514107)

**Search for Song**  
![Search for Song](https://github.com/prakhar450/vivpro-assgn/assets/55326021/0620f4c2-d832-4c14-85ad-c8299571436e)

**Update Rating of a Song**  
![Update Rating of a Song](https://github.com/prakhar450/vivpro-assgn/assets/55326021/25d5b686-e1f5-4799-9dd0-f7044c6f5c11)


