class AudioResponse:

    def __init__(self, audio=None, audio_list=None, number_of_results=None, cursor=None):
        self.audio = audio
        self.audio_list = audio_list
        self.number_of_results = number_of_results
        self.cursor = cursor


class EditionResponse:

    def __init__(self, edition=None, edition_list=None, number_of_results=None, cursor=None):
        self.edition = edition
        self.edition_list = edition_list
        self.number_of_results = number_of_results
        self.cursor = cursor
