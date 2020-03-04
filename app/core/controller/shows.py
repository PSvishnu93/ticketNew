from flask import request
from flask_restplus import Resource

from app.core.util.dto.shows import Shows
from app.core.service.show_services import MovieShow

show_service = MovieShow()
api = Shows.api
_show_post = Shows.show_post

@api.route('/')
class ShowAdder(Resource):
    @api.response(201, 'Show added successfully')
    @api.doc("Add a new show")
    @api.expect(_show_post, validate=True)
    def post(self):
        """Adds a new show """
        data = request.json
        return show_service.add_show(data)
    def get(self):
        """ Get all shows """
        return show_service.get_shows()
@api.route('/<show_id>')
class ShowList(Resource):
    def get(self, show_id):
        return show_service.get_shows(show_id)
