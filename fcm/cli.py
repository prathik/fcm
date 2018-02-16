import click
from message_loaders import LocalMessageLoader
from message_loaders import LocalFunnyLoader
from message_loaders import LocalHackLoader

@click.command()
@click.option('--first', '-f', is_flag=True, help='Interesting first commit message')
@click.option('--hack', '-h', is_flag=True, help='Adds a joke that the commit is a hack')
@click.option('--message', '-m', help="Commit message to be appended with")
def main(first, hack, message):
    """Generates funny commit message for you"""
    loader = LocalMessageLoader() if first else LocalFunnyLoader()
    if first:
        loader = LocalMessageLoader()
    elif hack:
        loader = LocalHackLoader()
    else:
        loader = LocalFunnyLoader()

    cm = loader.get_message()

    if message:
        cm = """{}
===
{}""".format(message, cm)
    click.echo(cm)
