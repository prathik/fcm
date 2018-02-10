import click
from message_loaders import LocalMessageLoader
from message_loaders import LocalFunnyLoader

@click.command()
@click.option('--funny', '-f', is_flag=True, help='Generates a joke')
def main(funny):
    """Generates the first commit message for you"""
    loader = LocalFunnyLoader() if funny else LocalMessageLoader()
    click.echo(loader.get_message())
