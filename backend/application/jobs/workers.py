#setup of celery

from celery import Celery
from flask import current_app as app

celery=Celery("Application Tasks")


class ContextTask(celery.Task):
    def _call_(self, args,*kwargs):
        with app.app_context():
            return self.run(args,*kwargs)