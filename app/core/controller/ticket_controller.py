from flask import request
from flask_restplus import Resource
from app.core.util.dto.tickets import Tickets
from app.core.service.ticket_service import TicketService

api = Tickets.api
_tickets = Tickets.tickets
ticket_service = TicketService()


@api.route('/<show_id>/')
class Ticket(Resource):
    @api.response(201, 'Tickets added successfully')
    @api.doc("Add tickets for the show")
    @api.expect(Tickets.tickets, validate=True)
    def post(self, show_id):
        data = request.json
        return ticket_service.add_tickets(show_id, data)

    def get(self, show_id):
        return ticket_service.get_tickets(show_id)
