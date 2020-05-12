import grpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
import quran.endpoints.grpc.shared_pb2 as shared_entity
import quran.endpoints.grpc.edition_pb2_grpc as edition_rpc

channel = grpc.insecure_channel("localhost:50051")
stub = edition_rpc.EditionStub(channel)


def test_create_edition():
    edition = entity_proto.EditionEntity(id='edition-1', language='en', name='edition-name-1',
                                         translator='edition-english-name-1', type='Arabic', format='format-1',
                                         direction='direction-1')
    res = stub.CreateEdition(edition)
    assert res.data.edition.id == edition.id
    assert res.data.edition.language == edition.language
    assert res.data.edition.name == edition.name.title()
    assert res.data.edition.translator == edition.translator.title()
    assert res.data.edition.type == 'Arabic'
    assert res.data.edition.format == edition.format.title()
    assert res.data.edition.direction == edition.direction

    # Second insert
    edition = entity_proto.EditionEntity(id='edition-2', language='en', name='edition-name-1',
                                         translator='edition-english-name-1', type='Arabic', format='format-2',
                                         direction='direction-2')
    res = stub.CreateEdition(edition)
    assert res.data.edition.id == edition.id
    assert res.data.edition.language == edition.language
    assert res.data.edition.name == edition.name.title()
    assert res.data.edition.translator == edition.translator.title()
    assert res.data.edition.type == 'Arabic'
    assert res.data.edition.format == edition.format.title()
    assert res.data.edition.direction == edition.direction

    # Third insert with type Translation
    edition = entity_proto.EditionEntity(id='edition-3', language='en', name='edition-name-3',
                                         translator='edition-english-name-3', type='Translation', format='format-1',
                                         direction='direction-1')
    res = stub.CreateEdition(edition)
    assert res.data.edition.id == edition.id
    assert res.data.edition.language == edition.language
    assert res.data.edition.name == edition.name.title()
    assert res.data.edition.translator == edition.translator.title()
    assert res.data.edition.type == 'Translation'
    assert res.data.edition.format == edition.format.title()
    assert res.data.edition.direction == edition.direction


def test_get_all_edition():
    edition_stream = stub.GetAll(shared_entity.EmptyMessage())

    count = 0
    for edition in edition_stream.data.edition:
        assert edition.language in ['en']
        count = count + 1

    assert count >= 3


def test_find_edition_by_id():
    res = stub.FindEditionById(shared_entity.IDRequest(id='edition-1'))

    assert res.data.edition.id == 'edition-1'
    assert res.data.edition.name == 'Edition-Name-1'


def test_find_edition_by_language():
    edition_stream = stub.FindEditionByLanguage(shared_entity.NameRequest(name='en'))

    for edition in edition_stream.data.edition:
        assert edition.language == 'en'


def test_find_edition_by_name():
    edition_stream = stub.FindEditionByName(shared_entity.NameRequest(name='edition-name-1'))

    for edition in edition_stream.data.edition:
        assert edition.name == 'Edition-Name-1'


def test_find_edition_by_translator():
    edition_stream = stub.FindEditionByTranslator(shared_entity.NameRequest(name='edition-english-name-1'))

    for edition in edition_stream.data.edition:
        assert edition.translator == 'Edition-English-Name-1'


def test_find_edition_by_type():
    edition_stream = stub.FindEditionByType(shared_entity.NameRequest(name='Arabic'))

    for edition in edition_stream.data.edition:
        assert edition.type == 'Arabic'


def test_find_edition_by_format():
    edition_stream = stub.FindEditionByFormat(shared_entity.NameRequest(name='format-1'))

    for edition in edition_stream.data.edition:
        assert edition.format == 'Format-1'
