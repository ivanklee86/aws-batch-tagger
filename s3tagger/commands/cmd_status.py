import click
from s3tagger import constants


@click.command()
def cli() -> None:
    """Prints information about s3tagger configuration."""
    click.echo("📝 s3tagger Status 📝")
    click.echo("Version: %s" % constants.VERSION)
