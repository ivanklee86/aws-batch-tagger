import os
import pytest
from s3tagger.utilities import queueing

BUCKET_NAME = "test"


def test_queue_lifecycle():
    my_queue = queueing.create_queue(bucket_name=BUCKET_NAME, new=True)
    assert os.path.exists(my_queue.path)
    assert os.path.isfile(os.path.join(my_queue.path, "data.db"))

    with pytest.raises(Exception):
        queueing.create_queue(bucket_name=BUCKET_NAME)

    queueing.delete_queue(bucket_name=BUCKET_NAME)
    assert not os.path.exists(my_queue.path)
    assert not os.path.isfile(os.path.join(my_queue.path, "data.db"))
