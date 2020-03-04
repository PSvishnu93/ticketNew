from app.core import db

class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    screen_id = db.Column(db.Integer, db.ForeignKey('screen.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    show_time = db.Column(db.DateTime, nullable=False)

class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'))
    seat_id = db.Column(db.Integer, db.ForeignKey('layout.id'))
    price = db.Column(db.Float, nullable=False)
    ticket_status = db.Column(db.Integer, db.ForeignKey('ticket_status.id'))

class TicketStatus(db.Model):
    __tablename__ = 'ticket_status'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
