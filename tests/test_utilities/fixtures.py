import pytest
import aaptivsecrets
from click.testing import CliRunner
from s3tagger.cli import Context


@pytest.fixture()
def runner():
    yield CliRunner()


@pytest.fixture()
def click_context():
    ctx = Context()
    ctx.config = aaptivsecrets.get_env_var_dict_for_app("dev", "ios")
    yield ctx
