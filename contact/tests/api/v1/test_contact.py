from algonaut.tests.helpers import ApiTest
from algonaut.settings import settings
import requests
import re

from sqlalchemy.sql import and_

class TestContact(ApiTest):

    def test_contact(self):

        data = {
            'email' : 'max@mustermann.de',
            'extra_data' : {
                'foo' : 'bar',
            }
        }

        response = requests.post(self.url('/contact/submit'), json=data)

        assert response.status_code == 200

        email = self.test_queue.get(True, timeout=2.0)
        assert email['type'] == 'email'

        message = email['data']
        for part in message.walk():
            text = part.get_payload(decode=True)
            if not text:
                continue
            assert b'max@mustermann.de' in text
            assert b'foo' in text

    def test_extra_data(self):
        pass