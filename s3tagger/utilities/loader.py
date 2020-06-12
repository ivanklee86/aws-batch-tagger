import boto3
from alive_progress import alive_bar
from persistqueue import SQLiteAckQueue

S3 = boto3.client('s3')


def get_files(bucket_name: str, queue: SQLiteAckQueue, contains: tuple, not_contains: tuple = None) -> None:
    paginator = S3.get_paginator("list_objects_v2")

    with alive_bar() as bar:
        for page in paginator.paginate(Bucket=bucket_name):
            for file in page['Contents']:
                if any(n.lower() in file['Key'].lower() for n in contains):
                    if not_contains:
                        if not any(n.lower() in file['Key'].lower() for n in not_contains):
                            queue.put(file['Key'])
                    else:
                        queue.put(file['Key'])

            bar()
