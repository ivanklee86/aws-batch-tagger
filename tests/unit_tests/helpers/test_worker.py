import boto3
import uuid
from s3tagger.utilities import worker
from tests.test_utilities import constants


def test_worker(populated_queue):
    test_file = "test.txt"
    test_tag = f"test_{uuid.uuid4()}"
    q = populated_queue

    worker.worker(bucket=constants.BUCKET_NAME, queue=q, tags={"test": test_tag})

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
        assert test_pair['Value'] == test_tag
