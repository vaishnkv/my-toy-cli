import click

@click.group()
def strutils():
    pass
    

@strutils.command()
@click.argument("input_str",type=str)
def reverese(input_str : str):
    """Reverse the given string"""
    click.echo(f"\n Reversed string is  :  {''.join(list(reversed(input_str)))}\n")

@strutils.command()
@click.argument("input_str",type=str)
def trim(input_str : str):
    """ Trim the whitespace from the given string"""
    click.echo(f"\n Striped Version is :  {input_str.strip()}\n")



# Additional commands can be added here 
