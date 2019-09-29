from myservice.app import app as tested_app
import unittest
import json


class TestSomething(unittest.TestCase):

    def test_home_view(self):
        # creating a FlaskClient instance to interact with the app
        tested_app.testing = True
        client = tested_app.test_client()

        # calling /hello endpoint
        hello = client.get('/hello')

        # asserting the body
        body = json.loads(str(hello.data, 'utf8'))
        self.assertEqual(body['Hello'], 'World')
