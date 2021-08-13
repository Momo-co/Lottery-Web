from flask import url_for
from flask_testing import TestCase

from service_4.app import app, prizes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_gen_prize(self):

        for colour in prizes['colour']:
            for number in prizes['number']:

                lucky_input = {'colour':colour, 'number':number}
                response = self.client.post(url_for('gen_prize'), json=lucky_input)

                self.assert200(response)

                expected_prize = prizes['colour'][colour] * prizes['number'][number]
                self.assertEqual(response.json, expected_prize)