from click.testing import CliRunner
from s3tagger.cli import cli
from tests.test_utilities import constants
from tests.test_utilities.fixtures import runner  # noqa: F401


def test_e2e_populate(runner, cleanup):  # noqa: F811
    runner = CliRunner()
    result = runner.invoke(cli, ["populate", "-b", constants.BUCKET_NAME, "-m", ".png", "-m", ".txt"])

    assert result.exit_code == 0
