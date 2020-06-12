import click
from s3tagger.cli import pass_context, Context
from s3tagger.utilities import queueing


@click.command()
@click.option('--bucket', '-b', default="", type=str, help="S3 bucket.")
@pass_context
def cli(ctx: Context, bucket: str) -> None:
    if queueing.check_queue(bucket):
        queueing.delete_queue(bucket)

        click.echo(f"🧹 Queue for {bucket} is cleaned up! 🧹")
    else:
        click.echo(f"🧹 No queue for {bucket} was found, doing nothing! 🧹")