from app.core import db
from app.core.factory import flask_bcrypt

class CinemaUser(db.Model):
    __tablename__ = 'cinema_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    public_id = db.Column(db.String(100), unique=True)
    registered_on = db.Column(db.DateTime, nullable=False)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'))

    @property
    def password(self):
        raise AttributeError('password: read-only field')
    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password, password)
    
    def __repr__(self):
        return "<User> '%s' '%s'".format(self.first_name, self.last_name)