import os
import appdirs
import persistqueue
import shutil
from rich import print
from s3tagger import constants


DATA_DIR = appdirs.user_data_dir(appname=constants.APP_NAME)


def create_queue(bucket_name: str, new: bool) -> persistqueue.SQLiteAckQueue:
    queue_folder = os.path.join(DATA_DIR, bucket_name)

    if new:
        if os.path.exists(queue_folder):
            print(f"[dark_red]Warning![/dark_red] Working folder for {bucket_name} already exists at {queue_folder}")
            raise Exception("Queue folder already exists!")
        else:
            os.makedirs(queue_folder)

    return persistqueue.SQLiteAckQueue(queue_folder, multithreading=True)


def check_queue(bucket_name: str) -> bool:
    queue_folder = os.path.join(DATA_DIR, bucket_name)
    return os.path.exists(queue_folder)

def delete_queue(bucket_name: str) -> None:
    shutil.rmtree(os.path.join(DATA_DIR, bucket_name))
