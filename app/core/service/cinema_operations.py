from app.core import db
from app.core.models.cinema import Cinema, Screen, Layout
from app.core.models.shows_tickets import Show
from app.core.service.movie_services import MovieService
from datetime import datetime
from datetime import timedelta


class CinemaService:
    movie_servicer = MovieService()

    def get_cinema_shows(self, cinema_id):
        response = dict()
        response['screens'] = []
        screens = Screen.query.filter_by(cinema_id=cinema_id).all()
        for screen in screens:
            screen_dict = dict()
            screen_dict['id'] = screen.id
            screen_dict['name'] = screen.name
            screen_dict['shows'] = []
            min_date = datetime.now()
            max_date = datetime.today()+timedelta(2)
            shows = Show.query.filter(Show.screen_id == screen.id,
                                      Show.show_time <= max_date,
                                      Show.show_time >= min_date).all()
            for show in shows:
                show_dict = dict()
                show_dict['id'] = show.id
                show_dict['show_time'] = str(show.show_time)
                movie = self.movie_servicer.get_movie(show.movie_id)
                show_dict['movie'] = movie
                screen_dict['shows'].append(show_dict)
            response['screens'].append(screen_dict)
        return response, 200

    def save_screen_layout(self, screen_id, data):
        if Layout.query.filter_by(screen_id=screen_id).all():
            response = {"status": "fail",
                        "message": " Layout already added"}, 201
        else:
            response = {"status": "success",
                        "message": "Layout added successfully"}, 200
        new_seats = []
        for seat in data['seats']:
            new_seat = Layout(screen_id=screen_id,
                              row=seat['row'],
                              seat=seat['seat'],
                              x_cordinate=seat['x_cordinate'],
                              y_cordinate=seat['y_cordinate'])
            new_seats.append(new_seat)
        db.session.bulk_save_objects(new_seats)
        db.session.commit()
        return response

    def get_screen_layout(self, screen_id):
        layout = Layout.query.filter_by(screen_id=screen_id).all()
        response = dict()
        if layout:
            response['screen_id'] = screen_id
            response['seats'] = []
            for seat in layout:
                temp = {"id": seat.id,
                        "row": seat.row,
                        "seat": seat.seat,
                        "x_cordinate": seat.x_cordinate,
                        "y_cordinate": seat.y_cordinate}
                response['seats'].append(temp)
        if layout:
            return response, 200
        else:
            return response, 400

    def get_cinemas_in_city(self, city_id):
        cinema = Cinema.query.filter_by(city_id=city_id).all()
        return cinema

    def get_cinema_information(self, cinema_id):
        cinema = Cinema.query.filter_by(id=cinema_id).first()
        response = {}
        if cinema:
            response = {"id": cinema.id,
                        "name": cinema.name,
                        }
        return response

    def get_screen_information(self, screen_id):
        screen = Screen.query.filter_by(id=screen_id).first()
        response = {}
        if screen:
            response = {'id': screen.id,
                        'name': screen.name,
                        'cinema': self.get_cinema_information(screen.cinema_id)
                        }
        return response

    def get_seat_information(self, seat_id):
        seat = Layout.query.filter_by(id=seat_id).first()
        response = {}
        if seat:
            response = {"id": seat.id,
                        "row": seat.row,
                        "seat": seat.seat,
                        "x_cordinate": seat.x_cordinate,
                        "y_cordinate": seat.y_cordinate}
        return response

    def get_screens_of_cinema(self, cinema_ids):
        return Screen.query.filter(Screen.cinema_id.in_(cinema_ids)).all()

    def save_changes(self, new_show):
        db.session.add(new_show)
        db.session.commit()
