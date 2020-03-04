from app.core.models.movie import Movie, Language, Genre, Certificate


class MovieService:
    def get_movie(self, id):
        movie = Movie.query.filter_by(id=id).first()
        if movie:
            language = Language.query.filter_by(id=movie.language_id).first().name
            genre = Genre.query.filter_by(id=movie.genre_id).first().name
            certificate = Certificate.query.filter_by(id=movie.certificate_id).first().name
        out_dict = {
            "id": id,
            "name": movie.name,
            "language": language,
            "genre": genre,
            "certificate": certificate
        }
        return out_dict

