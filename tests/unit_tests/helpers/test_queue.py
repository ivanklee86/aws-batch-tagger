import os
import pytest
from s3tagger.utilities import queue

BUCKET_NAME = "test"


def test_queue_lifecycle():
    my_queue = queue.create_queue(bucket_name=BUCKET_NAME)
    assert os.path.exists(my_queue.path)
    assert os.path.isfile(os.path.join(my_queue.path, "data.db"))

    with pytest.raises(Exception):
        queue.create_queue(bucket_name=BUCKET_NAME)

    queue.delete_queue(bucket_name=BUCKET_NAME)
    assert not os.path.exists(my_queue.path)
    assert not os.path.isfile(os.path.join(my_queue.path, "data.db"))
