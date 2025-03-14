import click


@click.group()
def cli() -> None:
    pass


@click.group()
def group1() -> None:
    pass


@click.group()
def group2() -> None:
    pass


@group1.command()
def subcommand1() -> None:
    click.echo("Subcommand 1 in Group 1")


@group1.command()
def subcommand2() -> None:
    click.echo("Subcommand 2 in Group 1")


@group2.command()
def subcommand3() -> None:
    click.echo("Subcommand 3 in Group 2")


@group2.command()
def subcommand4() -> None:
    click.echo("Subcommand 4 in Group 2")


cli.add_command(group1)
cli.add_command(group2)

if __name__ == "__main__":
    cli()
