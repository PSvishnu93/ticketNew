from app.core import db
class Cinema(db.Model):
    __tablename__ = 'cinema'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    cordinates = db.Column(db.String(100), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))

class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    state_id = db.Column(db.Integer, db.ForeignKey('state.id'))

class State(db.Model):
    __tablename__ = 'state'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

class Screen(db.Model):
    __tablename__ = 'screen'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'))

class Layout(db.Model):
    __tablename__ = 'layout'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    screen_id = db.Column(db.Integer, db.ForeignKey('screen.id'))
    row = db.Column(db.String(10), nullable=False)
    seat = db.Column(db.String(10), nullable=False) 
    x_cordinate = db.Column(db.Integer, nullable=False)
    y_cordinate = db.Column(db.Integer, nullable=False)