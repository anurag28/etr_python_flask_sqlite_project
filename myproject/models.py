from myproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='audience', lazy=True)

    def __init__(self, name, email, username, password):
        self.name = name
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Name : {self.name} and Email is : {self.email}"


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    cast = db.Column(db.String(128), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String, nullable=False)
    review = db.Column(db.Text)
    posts = db.relationship('Post', backref='post_movie', lazy=True)

    def __init(self, name, cast, rating, genre):
        self.name = name
        self.cast = cast
        self.rating = rating
        self.genre = genre

    def __repr__(self):
        return f"Movie : {self.name}"


class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    artist = db.Column(db.String(128), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String, nullable=False)
    review = db.Column(db.Text)
    posts = db.relationship('Post', backref='post_song', lazy=True)

    def __init(self, name, artist, rating, genre):
        self.name = name
        self.artist = artist
        self.rating = rating
        self.genre = genre

    def __repr__(self):
        return f"Songs : {self.name}"


class Show(db.Model):
    __tablename__ = 'shows'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    cast = db.Column(db.String(128), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String, nullable=False)
    review = db.Column(db.Text)
    posts = db.relationship('Post', backref='post_show', lazy=True)

    def __init(self, name, cast, rating, genre):
        self.name = name
        self.cast = cast
        self.rating = rating
        self.genre = genre

    def __repr__(self):
        return f"Show : {self.name}"


class Post(db.Model):
    users = db.relationship(User)
    movies = db.relationship(Movie)
    shows = db.relationship(Show)
    songs = db.relationship(Song)

    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'))
    show_id = db.Column(db.Integer, db.ForeignKey('shows.id'))
