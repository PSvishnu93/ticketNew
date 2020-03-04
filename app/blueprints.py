from flask_restplus import Api
from flask import Blueprint

from app.core.controller.user_controller import api as user_ns
from app.core.controller.cinema_user import api as cinema_user_ns
from app.core.controller.cinema import api as cinema_op_ns
from app.core.controller.shows import api as show_op_ns
from app.core.controller.ticket_controller import api as ticket_ns
from app.core.controller.movie_search import api as movie_search_ns
from app.core.controller.buy_tickets import api as buy_ticket_ns


class AppBlueprint:
    blueprint = Blueprint('api', __name__)
    api = Api(blueprint,
              title='Online movie ticket booking',
              version='1.0',
              description='Flask restplus api for online movie ticket booking')
    api .add_namespace(user_ns)
    api.add_namespace(cinema_user_ns)
    api.add_namespace(cinema_op_ns)
    api.add_namespace(show_op_ns)
    api.add_namespace(ticket_ns)
    api.add_namespace(movie_search_ns)
    api.add_namespace(buy_ticket_ns)
