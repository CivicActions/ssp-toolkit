"""
Copyright 2019-2020 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/compliancetools#copyright.
"""
from pathlib import Path

import click
import yaml

from tools.helpers import ssptoolkit
from tools.helpers.ssp import Ssp
from tools.helpers.ssptoolkit import find_toc_tag
from tools.makefamilies.family import Control
from tools.makefamilies.makefamilies import create_family

project = ssptoolkit.get_project()


def get_family_data(output_to: str, family_data: dict) -> Ssp:
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


def get_standards() -> list:
    standards: list = []
    for std in project.standards:
        with open(Path(std), "r") as fp:
            std_data = yaml.safe_load(fp)
            standards.append(std_data.get("name"))
    return standards


def get_controls(control: Control) -> list:
    control_text: list = [
        f"### {control.control_id}: {control.control_name}",
        "```text",
        control.description,
        "```",
        f"**Status:** {control.status}",
    ]
    for key, part in control.parts.items():
        if key != "_default":
            control_text.append(f"#### {key}")
        for control_part in part:
            control_text.append(f"##### {control_part.party}")
            control_text.append(control_part.narrative)

    return control_text


def write_ssp(ssp_data: Ssp, output_to: str):
    text_output: list = [
        "<!--TOC-->",
        "<!--TOC-->",
        "",
        f"# {project.name} System Security Plan",
        "",
    ]
    standards = get_standards()
    for standard in standards:
        text_output.append(f"## {standard}")
    text_output.append("\n")

    for family in ssp_data.families:
        text_output.append(f"## {family.family_id}: {family.family_name}\n\n")
        controls = dict(sorted(family.controls.items()))
        for _, control in controls.items():
            control_text = get_controls(control)
            text_output.extend(control_text)
    ssp_file = Path(output_to).joinpath("ssp").with_suffix(".md")
    with open(ssp_file, "w+") as fp:
        fp.writelines([f"{line}\n" for line in text_output])
    find_toc_tag(file=str(ssp_file.as_posix()), levels=2)
    print(f"Wrote SSP to {ssp_file}")


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
    family_files = ssptoolkit.get_component_files(project.get_components())
    families = create_family(
        families=family_files, out_path=output_dir, return_data=True
    )
    ssp_data = get_family_data(output_to=output_dir, family_data=families)
    write_ssp(ssp_data=ssp_data, output_to=output_dir)


if __name__ == "__main__":
    main()
