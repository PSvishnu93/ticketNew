from app.core import db
from app.core.models.shows_tickets import Ticket, Show, TicketStatus
from app.core.service.cinema_operations import CinemaService
from app.core.models.cinema import Layout


class TicketService:
    cinema_service = CinemaService()

    def add_tickets(self, show_id, data):
        new_tickets = []
        responses = []
        show_info = Show.query.filter_by(id=show_id).first()
        if show_info is None:
            return [{
                    "show_id": show_id,
                    "status": "fail",
                    "message": "Invalid show"
                    }], 409
        for ticket in data['tickets']:
            seat_id = ticket['seat_id']
            seat_info = Layout.query.filter_by(id=seat_id).first()

            if seat_info is None or seat_info.screen_id != show_info.screen_id:
                response = {
                    "seat_id": seat_id,
                    "status": "fail",
                    "message": "Seat doesn't below to the show specified"
                }
            elif Ticket.query.filter_by(show_id=show_id, 
                                        seat_id=seat_id).first():
                response = {
                            "seat_id": seat_id,
                            "status": "fail",
                            "message": "Ticket already added for the seat"
                }
            else:
                new_ticket = Ticket(seat_id=seat_id,
                                    show_id=show_id,
                                    price=ticket['price'],
                                    ticket_status=ticket['status'])
                new_tickets.append(new_ticket)
                response = {
                            "seat_id": seat_id,
                            "status": "success",
                            "message": "Ticket added successfully"
                            }
            responses.append(response)
            return responses, 201
        self.save_changes(new_tickets)

    def get_tickets(self, show_id, status='all'):
        tickets = Ticket.query.filter_by(show_id=show_id).all()
        if not tickets:
            return {'status': 'fail',
                    'message': 'show not found'}, 404
        else:
            response = dict()
            response['show_id'] = show_id
            response['screen_id'] = Show.query.filter_by(id=show_id).first().screen_id
            response['tickets'] = []
            seat_availability = []
            cost_aggregate = dict()
            for ticket in tickets:
                temp = dict()
                temp['seat'] = self.cinema_service.get_seat_information(ticket.seat_id)
                temp['status'] = TicketStatus.query.filter_by(id=ticket.ticket_status).first().name
                if ticket.price not in cost_aggregate.keys():
                    cost_aggregate[ticket.price] = [0, 0]
                if temp['status'] == 'available':
                    cost_aggregate[ticket.price][0] += 1
                cost_aggregate[ticket.price][1] += 1
                temp['price'] = ticket.price
                response['tickets'].append(temp)
            for cost, availability in cost_aggregate.items():
                temp = {"price": cost,
                        'available_seats': availability[0],
                        "total_seats": availability[1]
                        }
                seat_availability.append(temp)
            response['seat_availability'] = seat_availability
        return response

    def update_ticket_status(self, ticket_ids, status):
        if status == 'in progress':
            ticket_status = 2
        elif status == 'reserved':
            ticket_status = 3
        elif status == 'cancelled':
            ticket_status = 1
        if Ticket.query.filter(Ticket.id.in_(ticket_ids), Ticket.ticket_status != 1).first() and status == 'in progress':
            return False
        else:
            Ticket.query.filter(Ticket.id.in_(ticket_ids)).update({Ticket.ticket_status:ticket_status},
                                synchronize_session=False)
            db.session.commit()
            return True

    def save_changes(self, data):
        db.session.bulk_save_objects(data)
        db.session.commit()
