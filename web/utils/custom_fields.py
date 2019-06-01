from django.db.models import CharField, TextField, DecimalField

from .utils import normalize_text

'''
set of custom filed to use in apps

'''


class FarsiCharField(CharField):
    """
    Farsi character field to change multi form characters reform to standard
    """

    def to_python(self, value):
        return super(FarsiCharField, self).to_python(normalize_text(value))


class FarsiTextField(TextField):
    """
        Farsi text field to change multi form characters reform to standard
    """

    def to_python(self, value):
        return super(FarsiTextField, self).to_python(normalize_text(value))


class LocationField(DecimalField):

    def __init__(self, *args, **kwargs):
        kwargs['max_digits'] = 11
        kwargs['decimal_places'] = 8
        super().__init__(*args, **kwargs)
