from app.core import db
from app.core.models.shows_tickets import Show
from app.core.service.movie_services import MovieService
from app.core.service.cinema_operations import CinemaService

from datetime import datetime, timedelta


class MovieShow:
    movie_service = MovieService()
    cinema_service = CinemaService()

    def add_show(self, data):
        if self.is_slot_available(data):
            new_show = Show(movie_id=data['movie_id'],
                            screen_id=data['screen_id'],
                            show_time=data['show_time'])
            self.save_changes(new_show)
            response_object = {
                'status': 'success',
                'message': 'Show added successfully'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Show time already used'
            }
            return response_object, 409

    def is_slot_available(self, data):
        show = Show.query.filter_by(show_time=data['show_time'],
                                    screen_id=data['screen_id']
                                    ).first()
        if show:
            return False
        else:
            return True

    def get_shows(self, show_id=None):
        now = datetime.now()
        if not show_id:
            shows = Show.query.filter(Show.show_time >= now)
        else:
            shows = Show.query.filter_by(id=show_id)
        response = dict()
        if shows:
            response['shows'] = []
            for show in shows:
                show_temp = dict()
                show_temp['id'] = show.id
                show_temp['show_time'] = str(show.show_time)
                show_temp['movie'] = self.movie_service.get_movie(show.movie_id)
                show_temp['screen'] = self.cinema_service.get_screen_information(show.screen_id)
                response['shows'].append(show_temp)
        return response

    def get_shows_by_screens(self, screen_ids, days=2):
        min_show_date, max_show_date = self.min_max_date(days)

        shows = Show.query.filter(Show.screen_id.in_(screen_ids),
                                  Show.show_time >= min_show_date,
                                  Show.show_time <= max_show_date
                                  ).all()
        return shows

    def get_show_by_screen_and_movie(self, screen_ids, movie_id, days=2):
        min_show_date, max_show_date = self.min_max_date(days)
        shows = Show.query.filter(Show.screen_id.in_(screen_ids),
                                  Show.show_time >= min_show_date,
                                  Show.show_time <= max_show_date,
                                  Show.movie_id == movie_id
                                  ).all()
        return shows

    def min_max_date(self, days):
        min_show_date = datetime.now()
        future_date = datetime.now().date()+timedelta(days=days)
        max_show_date = datetime(future_date.year, future_date.month,
                                 future_date.day, 23, 59, 59)
        return min_show_date, max_show_date

    def save_changes(self, new_show):
        db.session.add(new_show)
        db.session.commit()
