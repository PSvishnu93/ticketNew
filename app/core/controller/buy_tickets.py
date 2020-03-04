from flask import request
from flask_restplus import Resource

from app.core.util.dto.buy_tickets import BuyTicketDto
from app.core.service.buy_tickets import TicketBuyer


api = BuyTicketDto.api
_ticket = BuyTicketDto.tickets
_status_update = BuyTicketDto.status_update


@api.route('/<show_id>/')
class TicketReservation(Resource):
    ticket_buyer = TicketBuyer()
    @api.response(201, "Tickets added to the cart")
    @api.doc("Add tickets to cart")
    @api.expect(_ticket, validate=True)
    def post(self, show_id):
        data = request.json
        return self.ticket_buyer.add_tickets_to_cart(data, show_id)
    
    @api.response(201, "Reservation status changed")
    @api.doc("Confirm tickets")
    @api.expect(_status_update, validate=True)
    def put(self, show_id):
        data = request.json
        return self.ticket_buyer.cancel_or_reserve_tickets(data)
