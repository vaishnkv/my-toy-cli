import click
from module import datetime,strutils,randomfacts
from module.utils import print_command_tree


@click.group()
def toycli():
    """
    Welcome to toycli  !!
    
    provide keyname for the service that you are looking for
    
    example:
    
        toycli datetime 
    
    """
    pass

toycli.add_command(datetime)
toycli.add_command(randomfacts)
toycli.add_command(strutils)



if __name__ == '__main__':
    toycli()
    # print_command_tree(toycli)
    
    
