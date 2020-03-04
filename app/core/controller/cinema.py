from flask import request
from flask_restplus import Resource

from app.core.util.dto.cinemas import Cinema
from app.core.service.cinema_operations import CinemaService

cinema_show = CinemaService()
api = Cinema.api
_layout = Cinema.layout


@api.route('/<cinema_id>/shows/')
@api.param('cinema_id', 'Cinema id')
@api.response('404', 'Resource not found')
class ShowGetter(Resource):
    @api.doc("Get all shows in all screens")
    # @api.marshal_with(_show)
    def get(self, cinema_id):
        response = cinema_show.get_cinema_shows(cinema_id)
        if not response:
            api.abort(404)
        else:
            return response


@api.route('/screen/<screen_id>/layout')
@api.param('screen_id', 'Id of the screen')
@api.response('404', 'Resource not found')
class ScreenLayout(Resource):
    @api.doc("Get the screen layout")
    @api.marshal_with(_layout)
    def get(self, screen_id):
        response = cinema_show.get_screen_layout(screen_id)
        if not response:
            api.abort(404)
        else:
            return response

    @api.doc("Save layout")
    @api.expect(_layout, validate=True)
    def post(self, screen_id):
        data = request.json
        return cinema_show.save_screen_layout(screen_id, data)
