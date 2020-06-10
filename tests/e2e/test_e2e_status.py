from click.testing import CliRunner
from s3tagger.cli import cli
from tests.test_utilities.fixtures import runner  # noqa: F401


def test_e2e_status(runner):  # noqa: F811
    runner = CliRunner()
    result = runner.invoke(cli, ["status"])

    assert result.exit_code == 0
    assert "Version:" in result.output
