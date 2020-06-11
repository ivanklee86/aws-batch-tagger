import pytest
import aaptivsecrets
from click.testing import CliRunner
from s3tagger.cli import Context
from s3tagger.utilities import queueing

BUCKET_NAME = "aaptiv-warner-prod"

@pytest.fixture()
def runner():
    yield CliRunner()


@pytest.fixture()
def click_context():
    ctx = Context()
    ctx.config = aaptivsecrets.get_env_var_dict_for_app("dev", "ios")
    yield ctx

@pytest.fixture()
def queue():
    try:
        queueing.delete_queue(BUCKET_NAME)
    except:
        pass

    queue = queueing.create_queue(BUCKET_NAME, new=True)
    yield queue
    queueing.delete_queue(BUCKET_NAME)
