from fireo.fields import IDField, TextField
from fireo.models import Model


class Edition(Model):
    id = IDField()
    language = TextField()
    name = TextField(format='title')
    translator = TextField(format='title')
    type = TextField(format='capitalize')
    format = TextField(format='capitalize')
    direction = TextField()

    class Meta:
        to_lowercase = True