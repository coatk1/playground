"""Console script for flaskr."""

import click


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
# @click.option('--version', '-v', help='Get package version')
def cli():
    """A simple command line tool."""
    pass


@cli.command('run', short_help='Runs the application.')
# @click.version_option()
def run():

    click.echo('Running the application')
    # Launch application through URL or filetype.
    click.launch("http://127.0.0.1:5000/hello")
    click.echo('Exiting the application')

# cli.add_command(hello)


if __name__ == '__main__':
    cli()
