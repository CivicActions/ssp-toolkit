# Copyright 2019-2020 CivicActions, Inc. See the README file at the top-level
# directory of this distribution and at https://github.com/CivicActions/compliancetools#copyright.

import re
from pathlib import Path

import click
import yaml
from family import Control, Family, Part

from tools.lib.opencontrol import OpenControl


def sortable_control_id(control_id: str) -> str:
    return re.sub(r"(\d+)", lambda m: m.group(1).zfill(2), control_id)


def get_standards() -> tuple:
    try:
        with open("opencontrol.yaml", "r") as oc:
            project = yaml.load(oc, Loader=yaml.SafeLoader)
    except FileNotFoundError as error:
        print(f"File not found: {error}")

    standards: list = []
    for standard in project.get("standards"):
        with open(standard, "r") as s:
            standards.append(yaml.load(s, Loader=yaml.SafeLoader))

    title = project.get("metadata").get("description")
    return title, standards


def get_standards_control_data(control: str, standards: list) -> dict:
    also_try = control.replace("(", " (")
    for s in standards:
        if control_data := s.get(control):
            return control_data
        elif control_data := s.get(also_try):
            return control_data
    raise KeyError(f"Control {control} not found.")


def get_standards_family_name(family: str, standards: list) -> str:
    for s in standards:
        if control_data := s.get(family, None):
            return control_data.get("name")
    raise KeyError(f"Control {family} not found.")


def get_family_files(components: list) -> dict:
    family_files: dict = {}
    for c in components:
        with open(Path(c).joinpath("component.yaml"), "r") as cfp:
            component = yaml.load(cfp, Loader=yaml.SafeLoader)
        for family in component.get("satisfies"):
            component_file = Path().joinpath(c, family)
            family_name = component_file.stem
            if family_name not in family_files:
                family_files[family_name] = []
            family_files[family_name].append(component_file.as_posix())

    return family_files


def get_control_parts(parts: list, control: Control, parent: str) -> Control:
    for p in parts:
        part_id = p.get("key", "_default")
        control.add_part(
            part_id,
            Part(
                key=part_id,
                party=parent,
                narrative=p.get("text"),
            ),
        )
    return control


def get_controls(family_files: list, family: Family, standards: list) -> Family:
    base_path = Path()
    for component in family_files:
        component_file = base_path.joinpath(component)
        with open(component_file, "r") as cfp:
            comp_yaml = yaml.load(cfp, Loader=yaml.SafeLoader)
        parent = component_file.parents[0].name
        for s in comp_yaml.get("satisfies"):
            control_id = s.get("control_key")
            sort_id = sortable_control_id(control_id=control_id)
            standard_data = get_standards_control_data(control_id, standards)
            status = s.get("implementation_status", "incomplete")
            if sort_id in family.controls:
                control = family.controls.get(sort_id)
                get_control_parts(
                    parts=s.get("narrative"), control=control, parent=parent
                )
            else:
                control = Control(
                    control_id=control_id,
                    control_name=s.get("control_name"),
                    control_type=s.get("security_control_type"),
                    description=standard_data.get("description"),
                    status=status if status else "incomplete",
                    parts={},
                )
                control = get_control_parts(
                    parts=s.get("narrative"), control=control, parent=parent
                )
                family.add_control(cid=sort_id, control=control)
    return family


def create_family(families: dict, out_path: str):
    title, standards = get_standards()
    for key, family_files in families.items():
        fid = key[:2]
        family_name = get_standards_family_name(fid, standards)
        family = Family(
            title=title,
            family_id=fid,
            family_name=family_name,
            controls={},
        )
        family = get_controls(
            family_files=family_files, family=family, standards=standards
        )
        family.print_family_file(out_path=out_path)


@click.command()
@click.option(
    "--out",
    "-o",
    "output_dir",
    type=click.Path(exists=False, dir_okay=True, readable=True),
    default="docs/controls",
    help="Output directory (default: ./docs/controls)",
)
def main(output_dir):
    base = Path()
    controls_dir = base.joinpath(output_dir)
    if not controls_dir.exists():
        print(f"Creating output directory {controls_dir.resolve(strict=False)}")
        controls_dir.mkdir(exist_ok=False)

    oc_yaml = base.joinpath("opencontrol.yaml")
    if not oc_yaml.is_file():
        raise FileNotFoundError

    project = OpenControl.load(path=oc_yaml.as_posix())
    family_files = get_family_files(project.get_components())
    create_family(family_files, out_path=output_dir)
    print("Process complete.")


if __name__ == "__main__":
    main()
