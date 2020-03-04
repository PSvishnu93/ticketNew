from app.core.models.reservation import (UserReservation, ReservationStatus, 
                                         SeatReservation)
from app.core import db
from app.core.models.shows_tickets import Ticket

from app.core.service.ticket_service import TicketService
from datetime import datetime


class TicketBuyer:
    ticket_service = TicketService()

    def add_tickets_to_cart(self, data, show_id):
        user_id = data['user_id']
        num_of_seats = len(data['seats'])
        if num_of_seats > 0:
            seat_ids = [seat['seat_id'] for seat in data['seats']]
            tickets = Ticket.query.filter(Ticket.seat_id.in_(seat_ids),
                                          Ticket.show_id == show_id)
            ticket_ids = [ticket.id for ticket in tickets]
            if not self.ticket_service.update_ticket_status(ticket_ids,
                                                            status='in progress'):
                return {"status": "fail",
                        "message": "Seats no longer available"}
            price = sum([ticket.price for ticket in tickets])
            reserved_on = datetime.now()
            new_reservation = UserReservation(user_id=user_id,
                                              num_of_seats=num_of_seats,
                                              reserved_on=reserved_on,
                                              price=price,
                                              status_id=1)
            db.session.add(new_reservation)
            db.session.commit()

            for ticket_id in ticket_ids:
                new_seat = SeatReservation(ticket_id=ticket_id,
                                           user_reservation_id=new_reservation.id)
                db.session.add(new_seat)
                db.session.commit()
            return {"status": "success",
                    "reservation_id": new_reservation.id,
                    "message": "Tickets added to cart"}

    def cancel_or_reserve_tickets(self, data):
        reservation_id = data['user_reservation_id']
        reservation_status_id = ReservationStatus.query.filter_by(name=data['reservation_status']).first().id
        rows_affected = UserReservation.query.filter(UserReservation.id == reservation_id,
                                                     UserReservation.status_id == 1).update(
                                                     {UserReservation.status_id: reservation_status_id},
                                                     synchronize_session=False)
        if rows_affected == 0:
            return {"status": "fail",
                    "message": f"Ticket {data['reservation_status']} failed"}
        tickets = SeatReservation.query.filter_by(user_reservation_id=reservation_id).all()
        ticket_ids = [ticket.ticket_id for ticket in tickets]
        if self.ticket_service.update_ticket_status(ticket_ids,
                                                    data['reservation_status']):
            db.session.commit()
            return{"status": "success",
                   "message": f"""Ticket {data['reservation_status']}
                              successfully"""}
        else:
            return{"status": "fail",
                   "message": f"Ticket {data['reservation_status']} failed"}
