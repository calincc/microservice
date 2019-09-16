from flask import Blueprint
from flask.views import MethodView


home = Blueprint('home', __name__)


class Home(MethodView):
    def get(self):
        """Home view.

        This view will return an empty JSON mapping.
        """
        return {}
