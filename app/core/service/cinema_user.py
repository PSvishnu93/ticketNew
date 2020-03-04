from app.core import db
from app.core.models.cinema_user import CinemaUser

import uuid
import datetime


class CinemaUserService:
    def register(self, data):
        user_email = CinemaUser.query.filter_by(email=data['email']).first()
        user_phone = CinemaUser.query.filter_by(phone_number=data['phone_number']).first()
        if user_email:
            response_object = {
                'status': 'fail',
                'message': 'Email already exists',
            }
            return response_object, 409
        elif user_phone:
            response_object = {
                'status': 'fail',
                'message': 'Phone number already exists.',
            }
            return response_object, 409
        print(data['cinema_id'])
        new_user = CinemaUser(first_name=data['first_name'],
                              last_name=data['last_name'],
                              phone_number=data['phone_number'],
                              email=data['email'],
                              password=data['password'],
                              registered_on=datetime.datetime.utcnow(),
                              public_id=str(uuid.uuid4()),
                              cinema_id=int(data['cinema_id'])
                              )
        self.save_changes(new_user)
        response_object = {
                            'status': 'success',
                            'message': 'Successfully registered.'
                            }
        return response_object, 201

    def get_user(self, id):
        user = CinemaUser.query.filter_by(id=id).first()
        return user

    def save_changes(self, new_user):

        db.session.add(new_user)
        db.session.commit()
