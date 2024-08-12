import click
from datetime import datetime as date_time

@click.group()
def datetime():
    """  """
    
    """
    
    Tip :
    
        Use "datetime onlydate" for only date
        Use "datetime onlytime" for only time
    """

@datetime.command()
def complete():
    """List all S3 buckets."""
    click.echo(f"\nToday's Date is :  {date_time.now()}\n")

@datetime.command()
def onlytime():
    """ Get time only """
    click.echo(f"\n Current Time is :  {date_time.now().time()}\n")
    
@datetime.command()
def onlydate():
    """Get date only """
    click.echo(f"\nToday's Date is :  {date_time.now().date()}\n")




# Additional s3 subcommands can be added here...
