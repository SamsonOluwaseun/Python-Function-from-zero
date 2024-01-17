from mylib.bot import scrape
import click

@click.command()
@click.option('--count',default=1, help='Number of greetings. ')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
@click.option('length', prompt='Expected paragraph length',
              help='Length of the output from wikipedia')
def cli(name="Microsoft", length=1):
    result= scrape(name, sentences=length)
    return result

if __name__ == '__main__':
    cli()