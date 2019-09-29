from myservice.app import app as tested_app
import unittest
import json


class TestSomething(unittest.TestCase):

    def test_home_view(self):
        # creating a FlaskClient instance to interact with the app
        tested_app.testing = True
        client = tested_app.test_client()

        # calling / endpoint
        home = client.get('/')

        # asserting the body
        body = json.loads(str(home.data, 'utf8'))
        self.assertEqual(len(body), 0)
