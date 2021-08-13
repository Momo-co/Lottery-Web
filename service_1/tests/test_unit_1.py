from flask import url_for
from flask_testing import TestCase
from requests_mock import mock
import os

from service_1.application import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = "sqlite:///"
        )
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()

class TestResponse(TestBase):
    def test_index(self):

        with mock() as m:
            m.get('http://service-2:5000/get/colour', text='Green')
            m.get('http://service-3:5000/get/num', text='5')
            m.post('http://service-4:5000/gen/prize', json=500)

            response = self.client.get(url_for('index'))

            self.assert200(response)
            self.assertIn('Your lucky colour is Green and lucky number is 5, so you just won £500', response.data.decode())