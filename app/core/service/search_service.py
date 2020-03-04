from app.core import db
from app.core.models.cinema import City


from app.core.service.cinema_operations import CinemaService
from app.core.service.show_services import MovieShow
from app.core.service.movie_services import MovieService

from app.core.models.cinema import Cinema,Screen
from app.core.models.shows_tickets import Show


class MovieSearch:
    cinema_service = CinemaService()
    show_service = MovieShow()
    movie_service = MovieService()

    def get_movies_in_city(self, city_name, day=None):
        city = City.query.filter_by(name=city_name).first()
        response = dict()
        if city:
            city_id = city.id
            cinemas = self.cinema_service.get_cinemas_in_city(city_id)
            cinema_ids = [cinema.id for cinema in cinemas]
            screens = self.cinema_service.get_screens_of_cinema(cinema_ids)
            screen_ids = [screen.id for screen in screens]
            shows = self.show_service.get_shows_by_screens(screen_ids)
            movie_ids = set(show.movie_id for show in shows)
            response = dict()
            response['movies'] = []
            for movie_id in movie_ids:
                response['movies'].append(self.movie_service.get_movie(
                                          movie_id))
        return response, 200

    def get_shows_by_city_movie(self, city_name, movie_id, day=None):
        city = City.query.filter_by(name=city_name).first()
        response = dict()
        if not city:
            return {"status": "fail",
                    "message": "city not found"}
        else:
            city_id = city.id
            min_show_date, max_show_date = self.show_service.min_max_date(2)
            result = Cinema.query.join(Screen).join(Show).filter(
                                       Cinema.city_id == city_id, 
                                       Show.movie_id == movie_id,
                                       Show.show_time >= min_show_date,
                                       Show.show_time <= max_show_date).add_columns(Cinema.id,
                                       Cinema.name, Screen.id, Screen.name,
                                       Show.id, Show.show_time).all()
            results = dict()
            for row in result:
                cinema_id, cinema_name, screen_id, screen_name, show_id, show_time =row[1:]
                cinema_key = (cinema_id, cinema_name)
                if cinema_key not in results.keys():
                    results[cinema_key] = dict()
                screen_key = screen_id, screen_name
                if screen_key not in results[cinema_key].keys():
                    results[cinema_key][screen_key] = []
                results[cinema_key][screen_key].append([show_id, show_time])
            response = dict()
            response['cinemas'] = []
            for key in results.keys():
                cinema_temp = dict()
                cinema_temp['id'], cinema_temp['name'] = key
                cinema_temp['screens'] = []
                for scr in results[key].keys():
                    scr_temp = dict()
                    scr_temp['id'], scr_temp['name'] = scr
                    scr_temp['shows'] = []
                    for shw in results[key][scr]:
                        shw_temp = dict()
                        shw_temp['id'] = shw[0]
                        shw_temp['show_time'] = str(shw[1])
                        scr_temp['shows'].append(shw_temp)
                    cinema_temp['screens'].append(scr_temp)
                response['cinemas'].append(cinema_temp)
            return response, 200
