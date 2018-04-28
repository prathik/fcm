import click
from message_loaders import LocalMessageLoader
from message_loaders import LocalFunnyLoader
from message_loaders import LocalHackLoader
from signatures import get_signature
import git
import os

@click.command()
@click.option('--first', '-f', is_flag=True, help='Interesting first commit message')
@click.option('--hack', '-h', is_flag=True, help='Adds a joke that the commit is a hack')
@click.option('--signature', '-s', help='Adds an ascii signature to the commit')
@click.option('--message', '-m', help="Commit message to be appended with")
def main(first, hack, signature, message):
    """Generates funny commit message for you"""
    
    if first:
        loader = LocalMessageLoader()
    elif hack:
        loader = LocalHackLoader()
    else:
        loader = LocalFunnyLoader()

    cm = loader.get_message()

    signatures = {
        ""
    }

    if message:
        cm = """{}
===
{}""".format(message, cm)

    if signature:
        cm = """{}
===
{}""".format(cm, get_signature(signature))
        
    repo = git.Repo(os.getcwd())
    repo.git.commit('-am', cm)
                    
    # click.echo(cm)
