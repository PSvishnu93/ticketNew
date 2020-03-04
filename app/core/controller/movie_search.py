from flask_restplus import Resource

from app.core.util.dto.movie_search_dto import MovieSearchDto

from app.core.service.search_service import MovieSearch

api = MovieSearchDto.api
movie_search = MovieSearch()
@api.route('/<city>/movies/')
class MoviesList(Resource):
    def get(self, city):
        return movie_search.get_movies_in_city(city)


@api.route('/<city>/movies/<movie_id>/shows')
class MovieShowList(Resource):
    def get(self, city, movie_id):
        return movie_search.get_shows_by_city_movie(city, movie_id)
