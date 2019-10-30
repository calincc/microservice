import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask

sentry_sdk.init(
    dsn="https://2c8359fe1ba349829859e5b685bdb0a9@sentry.io/1778958",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)


@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0


if __name__ == '__main__':
    app.run()
