from app.core import db

class UserReservation(db.Model):
    __tablename__ = 'user_reservation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    num_of_seats = db.Column(db.Integer, nullable=False)
    reserved_on = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('reservation_status.id'))

class SeatReservation(db.Model):
    __tablename__ = 'seat_reservation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'))
    user_reservation_id = db.Column(db.Integer, db.ForeignKey('user_reservation.id'))

class ReservationStatus(db.Model):
    __tablename__ = 'reservation_status'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)