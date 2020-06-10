from s3tagger.utilities import aws


def test_queue_lifecycle(queue):
    q = queue
    aws.get_files("aaptiv-ivan-test", q, [".png"])
