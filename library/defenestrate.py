import click

from complianceio import opencontrol


@click.command()
@click.argument(
    "source",
    type=click.Path(exists=True, dir_okay=False, file_okay=True, resolve_path=True),
)
@click.argument(
    "dest",
    type=click.Path(dir_okay=True, exists=True, file_okay=False, resolve_path=True),
)
def main(source, dest):
    opencontrol.load(source, debug=True).save_as(dest)


if __name__ == "__main__":
    main()
