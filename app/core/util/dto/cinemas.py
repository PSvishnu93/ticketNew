from flask_restplus import Namespace, fields


class Cinema:
    api = Namespace("Cinema", path='/cinema/',
                    description="Cinemas information")
    seat = api.model('seat',
                     {'id': fields.Integer(required=False, 
                                           description='Id of the seat'),
                      'row': fields.String(required=True,
                                           description='name of the row'),
                      'seat': fields.String(required=True,
                                            descripton='Seat number'),
                      'x_cordinate': fields.Integer(required=True,
                                                    description='X value'),
                      'y_cordinate': fields.Integer(required=True,
                                                    description='Y value')
                      })

    layout = api.model('layout',
                       {
                        'screen_id': fields.Integer(required=True,
                                                    description='Screen id'),
                        'seats': fields.List(fields.Nested(seat))
                        })
