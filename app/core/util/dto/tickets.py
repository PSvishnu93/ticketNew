from flask_restplus import Namespace, fields


class Tickets:
    api = Namespace('Movie Tickets', path='/tickets/',
                    description="Show tickets addition")

    ticket_list = api.model('ticket_list',
                            {
                             'seat_id': fields.Integer(required=True,
                                                       description='Seat id'),
                             'price': fields.Float(required=True,
                                                   description='Ticket price'),
                             'status': fields.Integer(required=True, default=1)
                            })
    tickets = api.model('show_tickets',
                        {
                         'show_id': fields.Integer(required=True,
                                                   description="Show id"),
                         'tickets': fields.List(fields.Nested(ticket_list))
                        })
