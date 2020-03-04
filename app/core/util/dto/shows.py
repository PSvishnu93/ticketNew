from flask_restplus import Namespace, fields


class Shows:
    api = Namespace("Shows", path='/shows/',
                    description='Movie shows functionalities')
    show_post = api.model('show',
                          {
                           'movie_id': fields.Integer(required=True,
                                                      description='Movie ID'),
                           'screen_id': fields.Integer(required=True,
                                                       descirption='Screen ID'),
                           'show_time': fields.String(required=True,
                                                      description="Show timing")
                            }
                          )
