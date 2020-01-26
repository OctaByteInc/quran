from quran.domain.audio import Audio as AudioDomain


class AudioRepo:

    def __init__(self):
        self.data = [
            {
                'id': 'audio-id-1',
                'ayah_id': 'ayah-id-1',
                'edition_id': 'edition-id-1',
                'type': 'Arabic',
                'audio': 'Link to audio file for ayah id 1'
            },
            {
                'id': 'audio-id-2',
                'ayah_id': 'ayah-id-2',
                'edition_id': 'edition-id-1',
                'type': 'Arabic',
                'audio': 'Link to audio file for ayah id 2'
            },
            {
                'id': 'audio-id-3',
                'ayah_id': 'ayah-id-1',
                'edition_id': 'edition-id-2',
                'type': 'Arabic',
                'audio': 'Link to audio file for ayah id 1'
            },
            {
                'id': 'audio-id-4',
                'ayah_id': 'ayah-id-1',
                'edition_id': 'edition-id-1',
                'type': 'Translation',
                'audio': 'Link to audio file for ayah id 1'
            },
        ]

    def create(self, audio):
        self.data.append(audio.to_dict)
        return AudioDomain.from_dict(audio.to_dict())

    def find_by_id(self, id):
        for audio in self.data:
            if audio['id'] == id:
                return AudioDomain.from_dict(audio)

    def find_by_ayah_id(self, id):
        for audio in self.data:
            if audio['ayah_id'] == id:
                return AudioDomain.from_dict(audio)

    def find_by_edition_id(self, id):
        for audio in self.data:
            if audio['edition_id'] == id:
                yield AudioDomain.from_dict(audio)

    def find_arabic_audio(self, **kwargs):
        for audio in self.data:
            if audio['ayah_id'] == kwargs.get('ayah_id') \
                    and audio['edition_id'] == kwargs.get('edition_id') \
                    and audio['type'] == 'Arabic':
                return AudioDomain.from_dict(audio)

    def find_translation_audio(self, **kwargs):
        for audio in self.data:
            if audio['ayah_id'] == kwargs.get('ayah_id') \
                    and audio['edition_id'] == kwargs.get('edition_id') \
                    and audio['type'] == 'Translation':
                return AudioDomain.from_dict(audio)