import os

from flask import Flask
from konfig import Config
from views import blueprints


_HERE = os.path.dirname(__file__)
_SETTINGS = os.path.join(_HERE, 'settings.ini')

configuration = Config(_SETTINGS)
app = Flask(__name__)
app.config.update(configuration.get_map('flask'))

for blueprint in blueprints:
    app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run()
