from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('User', path='/user',
                    description='User registration and information')
    user = api.model('user', {
        'email': fields.String(required=True,
                               description='Email for registration'),
        'first_name': fields.String(required=True,
                                    description='User first name'),
        'last_name':  fields.String(required=True,
                                    description='User last name'),
        'phone_number': fields.String(requierd=True,
                                      description='User phone number'),
        'password': fields.String(required=True,
                                  description='user password')
    })
