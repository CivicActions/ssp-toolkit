"""
Copyright 2019-2024 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

from pathlib import Path
from typing import Generator

from tools.helpers import ssptoolkit
from tools.helpers.project import Project
from tools.makefamilies.family import Control, Family, Part

project = Project()
controls_dir = Path("docs/controls")


def get_control_parts(parts: list, control, parent: str) -> Control:
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


def get_controls(family: Family, standards: list) -> Family:
    component_name = (
        f"{family.family_id}-{family.family_name.replace(' ', '_').upper()}"
    )
    component_controls = project.sort_component_controls(component_name=component_name)
    for key, control_id in project.controls[family.family_id].items():
        standard = get_standard_by_control_id(
            control_id=control_id, standards=standards
        )
        control = Control(
            control_id=control_id,
            control_name=standard.get("name"),
            description=standard.get("description"),
            status=standard.get("implementation_status", "incomplete"),
            parts={},
        )
        if key in component_controls:
            for parent, narrative, status, control_type in get_control_narratives(
                component_controls.get(key, {})
            ):
                get_control_parts(parts=narrative, control=control, parent=parent)
                update_status(control=control, status=status)
                update_control_type(control=control, control_type=control_type)
        family.add_control(cid=key, control=control)
    return family


def get_control_narratives(narratives: dict) -> Generator[tuple, None, None]:
    for narrative in narratives:
        key = list(narrative.keys())[0]
        text = narrative[key]
        yield key, text.get("narrative"), text.get("implementation_status"), text.get(
            "security_control_type"
        )


def update_status(control: Control, status: str):
    if not control.status:
        control.status = status
    elif control.status != "complete" and status == "complete":
        control.status = status
    else:
        control.status = status


def update_control_type(control: Control, control_type: str):
    control.control_type = control_type


def get_standard_by_control_id(control_id: str, standards: list) -> dict:
    for standard in standards:
        if control_id in standard:
            return standard[control_id]
    raise KeyError(f"{control_id} not found in standards.")


def create_toc(out_path: str | Path, controls: dict):
    toc_file = Path(out_path).parent.joinpath("controls").with_suffix(".md")
    with open(toc_file, "w+") as fp:
        for key, ctrl in controls.items():
            url_path = f"{Path(out_path).parts[-1]}/{key.upper()}.md"
            family_name = ctrl.get("name")
            family_anchor = family_name.lower().replace(" ", "-")
            fp.write(
                f"* [{key}: {family_name.title()}]({url_path}#{key.lower()}-{family_anchor})\n"
            )
            for control in ctrl.get("controls"):
                anchor = (
                    control.lower()
                    .replace("(", "")
                    .replace(")", "")
                    .replace(": ", "-")
                    .replace(" ", "-")
                )
                fp.write(f"\t* [{control}]({url_path}#{anchor})\n")
    print(f"TOC written to {toc_file.as_posix()}")


def create_family(return_data: bool = False) -> dict:
    title, standards = project.get_standards()
    families = ssptoolkit.get_component_files(project.project.get_components())
    toc: dict = {}
    families_data: dict = {}
    for key, family_files in families.items():
        fid = key[:2]
        family_name = ssptoolkit.get_standards_family_name(fid, standards)
        family = get_controls(
            family=Family(
                title=title,
                family_id=fid,
                family_name=family_name,
                controls={},
            ),
            standards=standards,
        )
        if return_data:
            families_data[key] = family
        else:
            family.print_family_file(out_path=controls_dir)
            toc[f"{fid}"] = {
                "name": family_name,
                "controls": [
                    f"{c.control_id.upper()}: {c.control_name}"
                    for _, c in family.controls.items()
                ],
            }
    if not return_data:
        create_toc(out_path=controls_dir, controls=toc)
    return families_data


def main():
    if not controls_dir.exists():
        print(f"Creating output directory {controls_dir.resolve(strict=False)}")
        controls_dir.mkdir(parents=True, exist_ok=False)
    create_family()
    print("Process complete.")


if __name__ == "__main__":
    main()
