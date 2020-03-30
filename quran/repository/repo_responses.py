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


class ImageResponse:

    def __init__(self, image=None, number_of_results=None):
        self.image = image
        self.number_of_results = number_of_results


class SurahResponse:

    def __init__(self, surah=None, surah_list=None, number_of_results=None, cursor=None):
        self.surah = surah
        self.surah_list = surah_list
        self.number_of_results = number_of_results
        self.cursor = cursor


class TranslationResponse:

    def __init__(self, translation=None, translation_list=None, number_of_results=None, cursor=None):
        self.translation = translation
        self.translation_list = translation_list
        self.number_of_results = number_of_results
        self.cursor = cursor