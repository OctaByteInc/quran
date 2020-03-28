import grpc
import quran.endpoints.grpc.entity_pb2 as entity_proto
import quran.endpoints.grpc.shared_pb2 as shared_entity
import quran.endpoints.grpc.surah_pb2_grpc as surah_rpc
import quran.endpoints.grpc.surah_pb2 as surah_proto

channel = grpc.insecure_channel("localhost:50051")
stub = surah_rpc.SurahStub(channel)


def test_create_surah():
    surah = entity_proto.SurahEntity(id='surah-1', number=1, name='surah-name-1',
                                     english_name_translation='english-translation-name-1', number_of_ayahs=7,
                                     revelation_type='type-1')
    res = stub.CreateSurah(surah)
    assert res.data.id == surah.id
    assert res.data.number == surah.number
    assert res.data.english_name_translation == surah.english_name_translation.title()
    assert res.data.name == surah.name.title()

    surah = entity_proto.SurahEntity(id='surah-2', number=2, name='surah-name-2',
                                     english_name_translation='english-translation-name-2', number_of_ayahs=144,
                                     revelation_type='type-2')
    res = stub.CreateSurah(surah)
    assert res.data.id == surah.id
    assert res.data.number == surah.number
    assert res.data.english_name_translation == surah.english_name_translation.title()
    assert res.data.name == surah.name.title()


def test_get_all_surah():
    surah_stream = stub.GetAll(shared_entity.EmptyMessage())

    count = 0
    for surah in surah_stream.data:
        count += 1

    assert count >= 2


def test_find_surah_by_id():
    surah = stub.FindSurahById(shared_entity.IDRequest(id='surah-1'))

    assert surah.data.id == 'surah-1'


def test_find_surah_by_number():
    surah = stub.FindSurahByNumber(shared_entity.NumberRequest(number=1))

    assert surah.data.number == 1


def test_find_surah_by_name():
    surah = stub.FindSurahByName(shared_entity.NameRequest(name='surah-name-1'))

    assert surah.data.name == 'Surah-Name-1'


def test_find_surah_by_english_translation_name():
    surah = stub.FindSurahByEnglishName(shared_entity.NameRequest(name='english-translation-name-2'))

    assert surah.data.english_name_translation == 'English-Translation-Name-2'


def test_find_surah_by_revelation_type():
    surah_stream = stub.FindSurahByRevelationType(surah_proto.RevelationRequest(revelation_type='type-1'))

    for surah in surah_stream.data:
        assert surah.revelation_type == 'Type-1'
