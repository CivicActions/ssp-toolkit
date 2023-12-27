"""
Copyright 2019-2020 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/compliancetools#copyright.
"""
from pathlib import Path

import click
import yaml
from complianceio.opencontrol import OpenControl

from tools.helpers import ssptoolkit
from tools.helpers.ssp import Ssp
from tools.makefamilies.makefamilies import create_family


def get_family_data(output_to: str, family_data: dict, project: OpenControl) -> Ssp:
    output = Path(output_to)
    if not output.exists():
        print(f"Creating output directory {output.as_posix()}")
        output.mkdir(exist_ok=False)
    families = [family for _, family in family_data.items()]
    return Ssp(
        name=project.name,
        standards=project.standards,
        families=families,
    )


def get_standard_name(standard: str) -> str:
    standard_path = Path(standard)
    with standard_path.open() as fp:
        sp = yaml.load(fp, Loader=yaml.SafeLoader)
    return sp.get("name")


def write_ssp(ssp_data: Ssp, output_to: str, project: dict):
    text = f"# {project.get('name')}\n\n"
    for standard in ssp_data.standards:
        name = get_standard_name(standard)
        text = text + f"## {name}\n"
    text = text + "\n"

    for family in ssp_data.families:
        text = text + f"## {family.family_id}: {family.family_name}\n\n"


@click.command()
@click.option(
    "--out",
    "-o",
    "output_dir",
    type=click.Path(exists=False, dir_okay=True, readable=True),
    default="docs",
    help="Output directory (default: ./docs)",
)
def main(output_dir: str):
    project = ssptoolkit.get_project()
    family_files = ssptoolkit.get_component_files(project.get_components())
    families = create_family(
        families=family_files, out_path=output_dir, return_data=True
    )
    ssp_data = get_family_data(
        output_to=output_dir, family_data=families, project=project
    )
    write_ssp(ssp_data=ssp_data, output_to=output_dir, project=project)


if __name__ == "__main__":
    main()
