from flask_restplus import Namespace, fields


class CinemaUserDto:
    api = Namespace('Cinema User', path='/cinema_user',
                    description='Registration of cinemas users')
    user = api.model('cinema',
                     {
                      'email': fields.String(required=True,
                                             description='Email for registration'),
                      'first_name': fields.String(required=True,
                                                  description='User first name'),
                      'last_name': fields.String(required=True,
                                                 description='User last name'),
                      'phone_number': fields.String(requierd=True,
                                                    description='User phone number'),
                      'password': fields.String(required=True,
                                                description='user password'),
                      'cinema_id': fields.Integer(required=True,
                                                  description='Id of the cinema')
                      })
