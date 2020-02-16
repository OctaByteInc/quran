from quran.domain.audio import Audio
from tests.quran.factory.audio_factory import AudioFactory


def test_audio_create():
    data = {
        'id': 'audio-id-5',
        'ayah_id': 'id_1',
        'edition_id': 'edition_1',
        'type': 'Translation',
        'audio': 'Link to audio file for ayah id 1'
    }
    audio = Audio.from_dict(data)
    create_audio = AudioFactory.create_audio()
    audio = create_audio.exec(audio)

    assert data == audio.to_dict()


def test_find_audio_id():
    find_audio = AudioFactory.find_audio()
    audio = find_audio.by_id('audio-id-1')

    assert audio.id == 'audio-id-1'


def test_find_audio_ayah_id():
    find_audio = AudioFactory.find_audio()
    audio = find_audio.by_ayah_id('ayah-id-1')

    assert audio.ayah_id == 'ayah-id-1'


def test_find_audio_edition_id():
    find_audio = AudioFactory.find_audio()
    audio_stream = find_audio.by_edition_id('edition-id-1')
    audio = next(audio_stream)

    assert audio.edition_id == 'edition-id-1'


def test_filter_arabic_audio():
    find_audio = AudioFactory.find_audio()
    audio = find_audio.arabic_audio(ayah_id='ayah-id-1', edition_id='edition-id-1')

    assert audio.ayah_id == 'ayah-id-1'
    assert audio.edition_id == 'edition-id-1'
    assert audio.type == 'Arabic'


def test_filter_translation_audio():
    find_audio = AudioFactory.find_audio()
    audio = find_audio.translation_audio(ayah_id='ayah-id-1', edition_id='edition-id-1')

    assert audio.ayah_id == 'ayah-id-1'
    assert audio.edition_id == 'edition-id-1'
    assert audio.type == 'Translation'
