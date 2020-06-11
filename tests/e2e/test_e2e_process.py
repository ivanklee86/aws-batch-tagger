import uuid
from click.testing import CliRunner
from s3tagger.cli import cli
from tests.test_utilities import constants
from tests.test_utilities.fixtures import runner  # noqa: F401


def test_e2e_process(runner, populated_queue):  # noqa: F811
    tag = f"test_{uuid.uuid4()}"
    runner = CliRunner()
    result = runner.invoke(cli, ["process", "-b", constants.BUCKET_NAME, "-t", f"test:{tag}"])

    assert result.exit_code == 0
    print(f"Tag: {tag}")
