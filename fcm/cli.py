import click
from message_loaders import LocalMessageLoader
from message_loaders import LocalFunnyLoader
from message_loaders import LocalHackLoader
from signatures import get_signature
import git
import os

def append_message(commit_message, append_string):
    return """{}
===
{}
""".format(commit_message, append_string)

@click.command()
@click.option('--first', '-f', is_flag=True, help='Interesting first commit message')
@click.option('--hack', '-h', is_flag=True, help='Adds a joke that the commit is a hack')
@click.option('--detailed', '-d', is_flag=True, help='Supports adding a detailed commit message')
@click.option('--signature', '-s', help='Adds an ascii signature to the commit')
@click.option('--message', '-m', help="Commit message to be appended with")
def main(first, hack, detailed, signature, message):
    """Generates funny commit message for you"""
    
    if first:
        loader = LocalMessageLoader()
    elif hack:
        loader = LocalHackLoader()
    else:
        loader = LocalFunnyLoader()

    cm = loader.get_message()

    if detailed:
        details = raw_input("What is this commit related to? ")
        testing = raw_input("How was this commit tested? ")
        server = raw_input("Is there any test environment this is deployed to? ")
        msg = """
Details = {}
Testing = {}
Hosted on = {}
""".format(details, testing, server)
        cm = append_message(msg, cm)

    if message:
        cm = append_message(message, cm)

    if signature:
        cm = append_message(cm,
                            get_signature(signature))
        
    repo = git.Repo(os.getcwd())
    repo.git.commit('-am', cm)
                    
    # click.echo(cm)
