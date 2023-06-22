import os
from datetime import datetime

from sqlalchemy import Float

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String)

class News(db.Model):
    idNews = db.Column(db.Integer, primary_key=True)
    titleNews = db.Column(db.String(255))
    bodyNews = db.Column(db.Text)
    imageNews = db.Column(db.LargeBinary, nullable=False)
    rendered_data = db.Column(db.Text, nullable=False)
    dateNews = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Game(db.Model):
    idGame = db.Column(db.Integer, primary_key=True)
    nameGame = db.Column(db.String(255), nullable=False)
    descriptionGame = db.Column(db.Text)
    bannerGame = db.Column(db.LargeBinary, nullable=False)
    rendered_data = db.Column(db.Text, nullable=False)
    trailerGame = db.Column(db.String(255))
    starsGame = db.Column(Float)

class Gamestore(db.Model):
    idGameStore = db.Column(db.Integer, primary_key=True)
    nameGameStore = db.Column(db.String(255), nullable=False)
    linkGameStore = db.Column(db.String(255))
    descriptionGamestore = db.Column(db.Text)

class GamestoreGame(db.Model):
    idGameStoreGame = db.Column(db.Integer, primary_key=True)
    idGame = db.Column(db.Integer)
    idGameStore = db.Column(db.Integer)
    priceGame = db.Column(Float)
    discountGame = db.Column(Float)