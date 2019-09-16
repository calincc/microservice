from flask import Blueprint
from flask.views import MethodView

hello = Blueprint('hello', __name__)


class Hello(MethodView):
    def get(self):
        """Hello view.

        This view will return a dummy JSON mapping.
        """
        return {"Hello": "World"}
