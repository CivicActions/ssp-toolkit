"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/compliancetools#license.
"""

from pathlib import Path

import click
from loguru import logger

from tools.helpers.family import Control
from tools.helpers.helpers import get_project_path, load_yaml_files
from tools.helpers.opencontrol import OpenControl
from tools.helpers.project import Project
from tools.helpers.ssp import Ssp
from tools.helpers.ssptoolkit import find_toc_tag
from tools.logging_config import setup_logging  # noqa: F401
from tools.create_files import create_files
from tools.make_families import make_families, create_family


def get_family_data(family_data: dict, write_to: Path, project: OpenControl) -> Ssp:
    if not write_to.exists():
        print(f"Creating output directory {write_to.as_posix()}")
        write_to.mkdir(exist_ok=False)
    families = [family for _, family in family_data.items()]
    standards = (
        list(project.standards.keys())
        if isinstance(project.standards, dict)
        else [standard for standard in project.standards if isinstance(standard, str)]
    )
    return Ssp(
        name=project.name,
        standards=standards,
        families=families,
    )


def get_standards(project: OpenControl) -> list:
    standards: list = []
    for std in project.standards:
        standard_path = get_project_path() / std
        std_data = load_yaml_files(file_path=standard_path)
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


def write_ssp(ssp_data: Ssp, write_to: Path, project: OpenControl):
    text_output: list = [
        "<!--TOC-->",
        "<!--TOC-->",
        "",
        f"# {project.name} System Security Plan",
        "",
    ]
    standards = get_standards(project=project)
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
    logger.info(f"Writing SSP to {ssp_file.as_posix()}")
    print(f"Wrote SSP to {ssp_file}")


def make_ssp():
    project_path = get_project_path()
    project = Project()
    write_to = project_path / "rendered" / "docs"
    controls_dir = write_to / "controls"
    create_files(templates="templates")
    make_families()
    families = create_family(
        controls_dir=controls_dir, project=project, return_data=True
    )
    ssp_data = get_family_data(
        family_data=families, write_to=write_to, project=project.project
    )
    write_ssp(ssp_data=ssp_data, write_to=write_to, project=project.project)


@click.command("make-ssp")
def make_ssp_cmd():
    """Generate a System Security Plan (SSP) from the control families."""
    make_ssp()
