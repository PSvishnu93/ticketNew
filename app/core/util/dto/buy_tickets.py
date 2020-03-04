from flask_restplus import Namespace, fields


class BuyTicketDto:
    api = Namespace('Buy Tickets', path='/buytickets/', 
                    description='Ticket booking platform')
    seat_list = api.model('seat_list',
                          {'seat_id': fields.Integer(required=True,
                                                     description="Seat id")
                           })
    tickets = api.model('tickets', {
        'user_id': fields.Integer(required=True, descirption="User id"),
        'seats': fields.List(fields.Nested(seat_list))
    })
    status_update = api.model('status',
                              {
                                'user_reservation_id': fields.Integer(required=True,
                                                                    description="User reservation id"),
                                'reservation_status': fields.String(required=True,
                                                                    description="Reservation status",
                                                                    enum=['reserved', 'cancelled'])
                                })
