from project.setup.db import models, db
from marshmallow import Schema, fields


class Genre(models.Base):
    __tablename__ = 'genres'

    name = db.Column(db.String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = "directors"

    name = db.Column(db.String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = "movies"

    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    trailer = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating  = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer,db.ForeignKey("genre.id"),nullable=False)
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"), nullable=False)
    director = db.relationship("Director")

class User(models.Base):
    __tablename__ = "users"

    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    surname = db.Column(db.String(100), unique=True, nullable=False)
    favorite_genre = db.Column(db.Integer)

