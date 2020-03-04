from app.core import db

class Language(db.Model):
    __tablename__ = 'language'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

class Certificate(db.Model):
    __tablename__ = 'certificate'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

class View(db.Model):
    __tablename__ = 'view'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(10), nullable=False, unique=True)

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.String(30), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    user_rating = db.Column(db.Float, default=0.0)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    certificate_id = db.Column(db.Integer, db.ForeignKey('certificate.id'))
    view_id = db.Column(db.Integer, db.ForeignKey('view.id'))   

