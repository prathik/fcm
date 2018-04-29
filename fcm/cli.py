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
@click.option('--author', '-a', is_flag=True, help="Update author of all commits")
def main(first, hack, detailed, signature, message, author):
    """Improving git experience"""

    if author:
        old_email = raw_input("Existing author email: ")
        author_name = raw_input("Author name for all commits: ")
        author_email = raw_input("New email of the author: ")
        os.system("""
git filter-branch --env-filter '
OLD_EMAIL="{}"
CORRECT_NAME="{}"
CORRECT_EMAIL="{}"
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
""".format(old_email, author_name, author_email))
        return;
    
    if first:
        loader = LocalMessageLoader()
    elif hack:
        loader = LocalHackLoader()
    else:
        loader = LocalFunnyLoader()

    cm = loader.get_message()

    if detailed:
        title = raw_input("Commit title: ")
        details = raw_input("What is this commit related to? ")
        testing = raw_input("How was this commit tested? ")
        server = raw_input("Is there any test environment this is deployed to? ")
        msg = """{}
Details = {}
Testing = {}
Hosted on = {}
""".format(title, details, testing, server)
        cm = append_message(msg, cm)

    if message:
        cm = append_message(message, cm)

    if signature:
        cm = append_message(cm,
                            get_signature(signature))
        
    repo = git.Repo(os.getcwd())
    repo.git.commit('-am', cm)
                    
    # click.echo(cm)
