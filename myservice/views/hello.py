from flask import Blueprint


hello = Blueprint('hello', __name__)


@hello.route('/hello')
def index():
    """Home view.

    This view will return an empty JSON mapping.
    """
    return {"Hello": "World"}
