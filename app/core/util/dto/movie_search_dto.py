from flask_restplus import Namespace


class MovieSearchDto:
    api = Namespace('Movie search', path='/',
                    description='Search for movies and shows in the city')
