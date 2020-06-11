from s3tagger.utilities import aws


def test_queue_lifecycle(queue):
    q = queue
    aws.get_files("aaptiv-ivan-test", q, [".png", ".txt"])

    initial_queue_size = q.size
    item = q.get()
    q.ack(item)
    assert q.size < initial_queue_size
