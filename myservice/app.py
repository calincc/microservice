import flask_profiler
import os

from dotenv import load_dotenv
from flasgger import Swagger
from flask import Flask, Blueprint
from flask_restful import Api
from konfig import Config
from myservice.views.home import Home
from myservice.views.hello import Hello

# Load application settings
_HERE = os.path.dirname(__file__)
_SETTINGS = os.path.join(_HERE, 'settings.ini')

# Load environment settings
load_dotenv()

configuration = Config(_SETTINGS)
app = Flask(__name__)
app.config.update(configuration.get_map('SomeSettingsSection'))
app.config["DEBUG"] = os.getenv('DEBUG')

# You need to declare necessary configuration to initialize flask-profiler as follows:
app.config["flask_profiler"] = {
    "enabled": app.config["DEBUG"],
    "storage": {
        "engine": "sqlite"
    },
    "basicAuth": {
        "enabled": True,
        "username": "admin",
        "password": "admin"
    },
    "ignore": [
        "^/static/.*"
    ]
}

api_bp = Blueprint('api', __name__)
api = Api(api_bp, catch_all_404s=True)

api.add_resource(Home, '/')
api.add_resource(Hello, '/hello')
app.register_blueprint(api_bp)
# swagger = Swagger(app)

# flask_profiler.init_app(app)
if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=int(os.getenv('PORT')), debug=bool(os.getenv('DEBUG')))
