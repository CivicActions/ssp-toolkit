"""
Copyright 2019-2020 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/compliancetools#copyright.
"""

from pathlib import Path

import click
import yaml

from tools.lib import ssptoolkit
from tools.makefamilies.family import Control, Family, Part


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


def get_controls(family_files: list, family: Family, standards: list) -> Family:
    base_path = Path()
    for component in family_files:
        component_file = base_path.joinpath(component)
        with open(component_file, "r") as cfp:
            comp_yaml = yaml.load(cfp, Loader=yaml.SafeLoader)
        parent = component_file.parents[0].name
        for s in comp_yaml.get("satisfies"):
            control_id = s.get("control_key")
            sort_id = ssptoolkit.sortable_control_id(control_id=control_id)
            standard_data = ssptoolkit.get_standards_control_data(control_id, standards)
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


def create_toc(out_path: str, controls: dict):
    toc_file = Path(out_path).parent.joinpath("controls").with_suffix(".md")
    with open(toc_file, "w+") as fp:
        for k, c in controls.items():
            url_path = f"{Path(out_path).parts[-1]}/{k.upper()}.md"
            family_name = c.get("name")
            family_anchor = family_name.lower().replace(" ", "-")
            fp.write(
                f"* [{k}: {family_name.title()}]({url_path}#{k.lower()}-{family_anchor})\n"
            )
            for control in c.get("controls"):
                anchor = (
                    control.lower()
                    .replace("(", "")
                    .replace(")", "")
                    .replace(": ", "-")
                    .replace(" ", "-")
                )
                fp.write(f"\t* [{control}]({url_path}#{anchor})\n")
    print(f"TOC written to {toc_file.as_posix()}")


def create_family(families: dict, out_path: str):
    title, standards = ssptoolkit.get_standards()
    toc: dict = {}
    for key, family_files in families.items():
        fid = key[:2]
        family_name = ssptoolkit.get_standards_family_name(fid, standards)
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
        toc[f"{fid}"] = {
            "name": family_name,
            "controls": [
                f"{c.control_id.upper()}: {c.control_name.title()}"
                for _, c in family.controls.items()
            ],
        }
    create_toc(out_path=out_path, controls=toc)


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

    project = ssptoolkit.load_project_data()
    family_files = ssptoolkit.get_component_files(project.get_components())
    create_family(family_files, out_path=output_dir)
    print("Process complete.")


if __name__ == "__main__":
    main()
