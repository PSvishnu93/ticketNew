import os
from app.core.factory import create_app
from app.core import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import unittest

from app.core.service.auto_ticket_canceller import AutoTicketCanceller
from app.blueprints import AppBlueprint
from flask_apscheduler import APScheduler


app = create_app(os.getenv('FLASK_ENV') or 'dev')

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
app.apscheduler.add_job(func=AutoTicketCanceller().cancel_tickets,
                        trigger='date',
                        id='auto_ticket_canceller')

app.register_blueprint(AppBlueprint.blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():    
    app.run()


@manager.command
def test():
    tests = unittest.TestLoader().discover('app/test', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    else:
        return 1


if __name__ == '__main__':
    manager.run()