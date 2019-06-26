from algonaut.api.resource import Resource
from algonaut.settings import settings
from ....tasks import send
from ..forms.contact import ContactForm
from flask import request

class Contact(Resource):

    def post(self):
        form = ContactForm(self.t, request.get_json() or {})
        if not form.validate():
            return {
                'message' : 'invalid data',
                'errors' : form.errors
            }, 400
        settings.delay(send, data=form.data)
        return {
            'message' : 'ok',
        }, 200
