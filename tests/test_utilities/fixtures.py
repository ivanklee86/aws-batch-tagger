import pytest
from click.testing import CliRunner
from s3tagger.utilities import queueing
from s3tagger.utilities import loader
from tests.test_utilities import constants


@pytest.fixture()
def runner():
    yield CliRunner()


@pytest.fixture()
def queue():
    try:
        queueing.delete_queue(constants.BUCKET_NAME)
    except:  # noqa: E722
        pass

    queue = queueing.create_queue(constants.BUCKET_NAME, new=True)
    yield queue
    queueing.delete_queue(constants.BUCKET_NAME)


@pytest.fixture()
def populated_queue(queue):
    q = queue
    loader.get_files(constants.BUCKET_NAME, q, (".png", ".txt"))
    yield q


@pytest.fixture()
def cleanup():
    try:
        queueing.delete_queue(constants.BUCKET_NAME)
    except:  # noqa: E722
        pass

    yield
    queueing.delete_queue(constants.BUCKET_NAME)
