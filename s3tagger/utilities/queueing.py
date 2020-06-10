import os
import appdirs
import persistqueue
import shutil
from rich import print
from s3tagger import constants

DATA_DIR = appdirs.user_data_dir(appname=constants.APP_NAME)

def create_queue(bucket_name: str, new: bool) -> persistqueue.SQLiteAckQueue:
    """
    Creates a SQLite-backed persistant ACK Queue in the user's data directory.

    :param bucket_name:
    :return:
    """
    queue_folder = os.path.join(DATA_DIR, bucket_name)

    if new:
        if os.path.exists(queue_folder):
            print(f"[dark_red]Warning![/dark_red] Working folder for {bucket_name} already exists at {queue_folder}")
            raise Exception("Queue folder already exists!")
        else:
            os.makedirs(queue_folder)

    return persistqueue.SQLiteAckQueue(queue_folder, multithreading=True)


def delete_queue(bucket_name: str) -> None:
    shutil.rmtree(os.path.join(DATA_DIR, bucket_name))
