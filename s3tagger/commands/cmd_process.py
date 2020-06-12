import threading
import click
from s3tagger.cli import pass_context, Context
from s3tagger.utilities import queueing, worker


@click.command()
@click.option('--workers', '-w', default=5, type=int, help="Number of threads to run in parallel.")
@click.option('--tags', '-t', type=str, multiple=True, help="Tags to put on objects.  Should be in the `KEY:VALUE' format e.g. '-m autodelete:true'")
@click.option('--bucket', '-b', default="", type=str, help="S3 bucket.")
@pass_context
def cli(ctx: Context, bucket: str, tags: tuple, workers: int) -> None:
    """Tags files in queue."""
    if not queueing.check_queue(bucket):
        raise click.UsageError(f"Queue for {bucket} does not exist!  Please run 's3transfer populate'.")

    tag_dict = {}
    for tag in tags:
        try:
            chunked_tag = tag.split(":")
            tag_dict[chunked_tag[0]] = chunked_tag[1]
        except:
            raise click.UsageError(f"Could not process tag of {tag}.  Please make sure it is in the KEY:VALUE format!")

    q = queueing.create_queue(bucket, new=False)

    threads = []
    for i in range(workers):
        t = threading.Thread(target=worker.worker, args=(i + 1, bucket, q, tag_dict))
        threads.append(t)
        t.start()

    for i in threads:
        i.join()

    click.echo(f"🎉 Tagging for {bucket} is complete! 🎉")
    click.echo(f"Tagged files ✅: {q.acked_count()}")
    click.echo(f"Failed files ❌: {q.ack_failed_count()}")
