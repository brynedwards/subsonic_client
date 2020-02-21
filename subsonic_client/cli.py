"""CLI interface."""
import sys
import click

from subsonic_client.client import Client
from subsonic_client import responses


@click.command()
@click.option("-b", "--base-url", help="Subsonic base URL.")
@click.option("-u", "--username", help="Subsonic username.")
@click.option("-p", "--password", help="Subsonic password.")
@click.option("-f", "--format", default="pretty", help="Output format.")
@click.option("-P", "--params", help="Parameters", type=(str, str), multiple=True)
@click.argument("command")
def main(base_url, username, password, format, command, params):
    """Makes requests to a Subsonic server."""
    client_format = "json"
    if format != "pretty":
        client_format = format
    instance = Client(base_url, username, password, "subsonic_client_cli", client_format)

    if hasattr(responses, command):
        print(getattr(instance, command)(params).pretty())
    return 0


if __name__ == "__main__":
    sys.exit(main(auto_envvar_prefix="SUBSONIC"))  # pragma: no cover
