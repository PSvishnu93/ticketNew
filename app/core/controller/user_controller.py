from flask import request
from flask_restplus import Resource
from app.core.util.dto.user_dto import UserDto

from app.core.service.user_service import UserService

user_service = UserService()
api = UserDto.api
_user = UserDto.user


@api.route('/register')
class UserList(Resource):
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
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
