from fireo.fields import IDField, NumberField, TextField
from fireo.models import Model


class Surah(Model):
    id = IDField()
    number = NumberField(int_only=True)
    name = TextField(format='title')
    english_name = TextField(format='title')
    english_name_translation = TextField(format='title')
    number_of_ayahs = NumberField(int_only=True)
    revelation_type = TextField(format='capitalize')

    class Meta:
        to_lowercase = True
