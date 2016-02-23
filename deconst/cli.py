import click

@click.command()
@click.option('--csv', '-c', is_flag=True, help='Output as Comma-Separated Values.')
@click.argument('name', default='world', required=False)
def main(auth, option):
    """Deconst Python CLI makes content and search commands simpler."""
