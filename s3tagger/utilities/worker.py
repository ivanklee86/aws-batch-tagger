import boto3
from persistqueue import SQLiteAckQueue


def worker(bucket: str, queue: SQLiteAckQueue, tags: dict) -> None:
    s3 = boto3.client('s3')
    version_paginator = s3.get_paginator('list_object_versions')

    while queue.size > 0:
        file = queue.get()

        try:
            for page in version_paginator.paginate(Bucket=bucket, Prefix=file):
                for version_info in page['Versions']:
                    tagging_args = {
                        'Bucket': bucket,
                        'Key': file,
                        'Tagging': {'TagSet': [{'Key': x, 'Value': tags[x] } for x in tags]}
                    }

                    if version_info['VersionId'] != 'null':
                        tagging_args['VersionId'] = version_info['VersionId']

                    s3.put_object_tagging(**tagging_args)
        except:
            queue.nack(file)

        queue.ack(file)
