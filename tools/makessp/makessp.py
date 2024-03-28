"""
Copyright 2019-2024 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/compliancetools#copyright.
"""
from pathlib import Path

import yaml

from tools.helpers import ssptoolkit
from tools.helpers.ssp import Ssp
from tools.helpers.ssptoolkit import find_toc_tag
from tools.makefamilies.family import Control
from tools.makefamilies.makefamilies import create_family

project = ssptoolkit.get_project()
write_to = Path("docs")


def get_family_data(family_data: dict) -> Ssp:
    if not write_to.exists():
        print(f"Creating output directory {write_to.as_posix()}")
        write_to.mkdir(exist_ok=False)
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
        f"#### {control.control_id}: {control.control_name}",
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


def write_ssp(ssp_data: Ssp):
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
        text_output.append(f"### {family.family_id}: {family.family_name}\n\n")
        controls = dict(sorted(family.controls.items()))
        for _, control in controls.items():
            control_text = get_controls(control)
            text_output.extend(control_text)
    ssp_file = Path(write_to).joinpath("ssp").with_suffix(".md")
    with open(ssp_file, "w+") as fp:
        fp.writelines([f"{line}\n" for line in text_output])
    find_toc_tag(file=str(ssp_file.as_posix()), levels=3)
    print(f"Wrote SSP to {ssp_file}")


def main():
    families = create_family(return_data=True)
    ssp_data = get_family_data(family_data=families)
    write_ssp(ssp_data=ssp_data)


if __name__ == "__main__":
    main()
