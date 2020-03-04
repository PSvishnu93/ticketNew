from flask import request
from flask_restplus import Resource
from app.core.util.dto.cinema_user_dto import CinemaUserDto

from app.core.service.cinema_user import CinemaUserService

user_service = CinemaUserService()
api = CinemaUserDto.api
_user = CinemaUserDto.user

@api.route('/register')
class UserList(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        print(data['cinema_id'])
        return user_service.register(data=data)

@api.route('/<id>')
@api.param('id', 'The user identifier')
@api.response('404', 'User not found')
class User(Resource):
    @api.doc("Get user")
    @api.marshal_with(_user)
    def get(self, id):
        user = user_service.get_user(id)
        if not user:
            api.abort(404)
        else:
            return user