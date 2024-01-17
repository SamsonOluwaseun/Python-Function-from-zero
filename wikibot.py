from mylib.bot import scrape
import click


@click.command()
@click.option("--name", prompt="Your name", help="The person to greet.")
@click.option(
    "--length",
    prompt="Expected paragraph length",
    help="Length of the output from wikipedia",
)
def cli(name="Microsoft", length="1"):
    result = scrape(name, length)
    click.echo(click.style(f"{result}:", fg="blue"))


if __name__ == "__main__":
    cli()
