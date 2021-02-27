import typer

"""
-CLI arguments are CLI parameters passes in specific order to a CLI application.
-CLI arguments are required by default
"""
# def main(name: str):
#     typer.echo(f"Hello {name}")

"""
CLI options are CLI parameters passed with a specific name
difference btn CLI option and a CLI argument the -- prepended to the name

To have a default last_name, provide a default value of ""
"""
def main(title: str,first_name: str, last_name: str = "", formal: bool = False):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """

    if formal:
        typer.echo(f"Hello {title} {first_name} {last_name}")
    else:
        typer.echo(f"Hello {first_name} {last_name}")

if __name__ == '__main__':
    typer.run(main)