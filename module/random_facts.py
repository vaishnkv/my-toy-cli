import click
import requests

URL_RANDOM = "https://uselessfacts.jsph.pl/api/v2/facts/random"
URL_TODAY="https://uselessfacts.jsph.pl/api/v2/facts/today"

@click.group()
def randomfacts():
    pass


@randomfacts.command()
def random():
    """ Get a random fact """
    # Make a POST request
    response = requests.get(URL_RANDOM)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        fact = response.json()
        click.echo(f"\nRandom Fact: { fact.get('text')}\n")
    else:
        click.echo(f"\nFailed to retrieve a fact. Status code: {response.status_code}")

@randomfacts.command()
def today():
    """ Get Today's Random Fact"""
    # Make a POST request
    response = requests.get(URL_TODAY)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        fact = response.json()
        click.echo(f"\nRandom Fact for the Day : { fact.get('text')}\n")
    else:
        click.echo(f"\nFailed to retrieve a fact. Status code: {response.status_code}")


# Additional s3 subcommands can be added here...
