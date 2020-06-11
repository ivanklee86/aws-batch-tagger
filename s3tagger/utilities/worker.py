import random
import boto3
from rich import print
from rich.color import ANSI_COLOR_NAMES
from persistqueue import SQLiteAckQueue


def worker(worker_id: int, bucket: str, queue: SQLiteAckQueue, tags: dict) -> None:
    s3 = boto3.client('s3')
    version_paginator = s3.get_paginator('list_object_versions')
    random_color = random.choice(list(ANSI_COLOR_NAMES.keys()))

    while not queue.empty():
        file = queue.get()

        try:
            for page in version_paginator.paginate(Bucket=bucket, Prefix=file):
                for version_info in page['Versions']:

                    tagging_args = {
                        'Bucket': bucket,
                        'Key': file,
                        'Tagging': {'TagSet': [{'Key': x, 'Value': tags[x]} for x in tags]}
                    }

                    if version_info['VersionId'] != 'null':
                        tagging_args['VersionId'] = version_info['VersionId']

                    print(f"[{random_color}]Worker {worker_id}[/{random_color}]: Processing {file} ({version_info['VersionId'] if version_info['VersionId'] != 'null' else 'Latest'})")

                    s3.put_object_tagging(**tagging_args)
        except:
            queue.nack(file)

        queue.ack(file)
