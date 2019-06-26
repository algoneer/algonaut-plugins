from algonaut.utils.forms import Form, Field
from algonaut.utils.forms.validators import (
    Optional,
    Regex,
    String,
    Required, 
    Boolean,
    ToLower,
    EMail,
    Length)

class ExtraData:

    def __call__(self, name, value, form):
        err = [form.t('form.invalid-extra-data')], None, True
        if not isinstance(value, dict):
            return err
        for k, v in value.items():
            if not isinstance(k, str):
                return err
            if not isinstance(v, (str, int, float)):
                return err

class ContactForm(Form):

    email = Field([Required(), String(), EMail(), ToLower()])
    name = Field([Optional(), String(), Length(min=2, max=50)])
    phone = Field([Optional(), String(), Regex(r'^[\d\+\-\/]{4,}$')])
    company = Field([Optional(), String(), Length(min=2, max=100)])
    extra_data = Field([Optional(), ExtraData()])
    test = Field([Optional(default=False), Boolean()])
