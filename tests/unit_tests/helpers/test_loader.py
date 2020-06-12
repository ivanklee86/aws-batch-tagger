from s3tagger.utilities import loader
from tests.test_utilities import constants


def test_queue_lifecycle(queue):
    q = queue
    loader.get_files(constants.BUCKET_NAME, q, (".png", ".txt"))

    initial_queue_size = q.size
    item = q.get()
    q.ack(item)
    assert q.size < initial_queue_size


def test_queue_notin(queue):
    q = queue
    loader.get_files(constants.BUCKET_NAME, q, (".png", ".txt"), ("incoming",))

    while not q.empty():
        item = q.get()
        assert "noti.txt" not in item
        q.ack(item)
