import boto3
import uuid
from click.testing import CliRunner
from s3tagger.cli import cli
from tests.test_utilities import constants
from tests.test_utilities.fixtures import runner  # noqa: F401


def test_e2e(runner):  # noqa: F811
    runner = CliRunner()
    test_file = "test.txt"
    tag = f"test_{uuid.uuid4()}"

    populate_result = runner.invoke(cli, ["populate", "-b", constants.BUCKET_NAME, "-m", ".png", "-m", ".txt"])
    process_result = runner.invoke(cli, ["process", "-b", constants.BUCKET_NAME, "-t", f"test:{tag}"])
    cleanup_result = runner.invoke(cli, ["clean", "-b", constants.BUCKET_NAME])

    assert populate_result.exit_code == 0
    assert process_result.exit_code == 0
    assert cleanup_result.exit_code == 0

    s3 = boto3.client('s3')
    versions_information = s3.list_object_versions(
        Bucket=constants.BUCKET_NAME,
        Prefix=test_file
    )

    for version in versions_information['Versions']:
        tagging = s3.get_object_tagging(
            Bucket=constants.BUCKET_NAME,
            Key=test_file,
            VersionId=version['VersionId']
        )

        [test_pair] = [x for x in tagging['TagSet'] if x['Key'] == 'test']
        assert test_pair['Value'] == tag
