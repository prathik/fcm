import click
from message_loaders import LocalMessageLoader
from message_loaders import LocalFunnyLoader

@click.command()
@click.option('--first', '-f', is_flag=True, help='Generates a joke')
def main(first):
    """Generates funny commit message for you"""
    loader = LocalMessageLoader() if first else LocalFunnyLoader()
    click.echo(loader.get_message())
