"""
Copyright 2019-2024 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#copyright.

Given a YAML file and path to directory of secrendered component files,
this tool generates Standard Operating Procedure (SOP) policy markdown files.
"""
import re
from dataclasses import dataclass
from datetime import date
from io import StringIO
from pathlib import Path

import click

from tools.helpers.ssptoolkit import load_template_args, load_yaml_files, write_toc
from tools.helpers.hash_checker.hash_checker import FileChecker


hashes = FileChecker()


@dataclass
class SopWriter:
    filepath: Path
    family: str
    controls: dict
    config: dict
    title: str

    def create_file(self):
        """
        Create a file stream to be used to be written to the markdown files.
        """
        try:
            self.output_file = StringIO()
            self.__write_header()
            self.__write_purpose()
            self.__write_scope()
            self.__write_controls()
            self.__write_file()
        finally:
            self.output_file.close()

    def __write_file(self):
        """
        Write the file with the table of contents to the filesystem.
        """
        print(f"Writing file to {self.filepath}")
        with open(self.filepath, "w+") as md:
            print(self.output_file.getvalue(), file=md)
        write_toc(self.filepath, levels=3)

    def __write_header(self):
        """
        Add the page header with generation date and TOC placeholder.
        """
        self.output_file.write(f"# {self.title}\n\n")
        self.output_file.write(f"*Reviewed and updated {date.today()}*\n\n")
        self.output_file.write("----\n\n")
        self.output_file.write("**Table of Contents**")
        self.output_file.write("\n<!--TOC-->\n\n----\n\n")
        self.output_file.write("## Introduction\n\n")

    def __write_purpose(self):
        self.output_file.write("### Purpose\n\n")
        self.output_file.write(self.config.get("sop").get(self.family).get("purpose"))
        self.output_file.write("\n\n")

    def __write_scope(self):
        self.output_file.write("### Scope\n\n")
        self.output_file.write(self.config.get("sop").get(self.family).get("scope"))
        self.output_file.write("\n\n")

    def __write_controls(self):
        """
        Write the controls to the file stream.
        """
        self.output_file.write("## Standards\n\n")
        for control_id, control in self.controls.items():
            self.output_file.write(f"### {control_id}\n\n")
            self.__write_text(control)
            self.__write_parts(control)

    def __write_text(self, control: dict):
        """
        Write the non-parts control narrative text.

        :param control: a dictionary of control narratives.
        """
        text = control.get("text", [])
        if text:
            prose = "\n\n".join(text)
            self.output_file.write(f"{prose}\n\n")

    def __write_parts(self, control: dict):
        """
        Write the control parts narrative text.

        :param control: a dictionary of control narratives.
        """
        for part, text in control.items():
            if part != "text":
                prose = "\n\n".join(text)
                self.output_file.write(f"**{part}.**\t{prose}\n")


def aggregate_control_data(component_dir: Path) -> dict:
    """
    Collect all the rendered Components YAML files and aggregate them by family.

    :param component_dir: a pathlib object file path object.
    :return: a dictionary with all the Controls sorted by Family.
    """
    families: dict = {}
    components = component_dir.rglob("*")
    templates = [
        comp_file
        for comp_file in components
        if comp_file.is_file() and comp_file.name not in ["component.yaml", "file_hashes.json"]
    ]

    for template in templates:
        family = template.stem.lower().replace("_", "-")
        if family not in families:
            families[family] = {"has_changes": False}

        has_changes = hashes.has_changed(template.as_posix())
        if not families[family]["has_changes"] and has_changes:
            families[family]["has_changes"] = True

        component = load_yaml_files(template)
        satisfies = component.get("satisfies", {})
        for control in satisfies:
            control_id = control.get("control_key")
            if "(" in control_id:
                control_key = create_sortable_id(control_id.strip().lower(), "extended")
            else:
                control_key = create_sortable_id(control_id.strip().lower(), "simple")
            control_name = control.get("control_name").title()
            key = f"{control_key} {control_name}"
            if key and key not in families[family]:
                families[family][key] = {}

            for parts in control.get("narrative"):
                part = parts.get("key", "text")

                if part not in families[family][key]:
                    families[family][key][part] = []
                families[family][key][part].append(parts.get("text"))

    write_families: dict = {}
    for f, v in families.items():
        if v.get("has_changes", False):
            del v["has_changes"]
            write_families[f] = v
    sort_controls(write_families)
    sort_parts(write_families)
    return write_families


def create_sortable_id(control_id: str, control_type: str = "simple") -> str:
    if control_type == "simple":
        match = re.match(r"^([a-z]{2})-(\d+)$", control_id)
    else:
        match = re.match(r"^([a-z]{2})-(\d+)\s*\((\d+)\)$", control_id)
    if match:
        family = match.group(1)
        number = int(match.group(2))
        extension = f"({int(match.group(3))})" if control_type == "extended" else ""
        return f"{family.upper()}-{str(number).zfill(2)}{extension}"


def write_files(families: dict, out_dir: Path, config: dict):
    """
    Write the Control Family data to markdown files.

    :param families: a dictionary of Controls sorted by Control Family.
    :param out_dir: a pathlib file path object where to write the files.
    :param config: a dictionary containing the configuration key values.
    """
    for family, controls in families.items():
        family_name = family[3:].replace("-", " ").title()
        filename = out_dir.joinpath(f"sop-{family}").with_suffix(".md")
        title = f"{family_name} ({family[:2].upper()}) Standard (SOP)"
        text = SopWriter(
            filepath=filename,
            family=family[:2].upper(),
            controls=controls,
            config=config,
            title=title,
        )
        text.create_file()


def sort_parts(families: dict) -> dict:
    """
    Sort the Control Parts so that they are ordered alphabetically.

    :param families: a dictionary of Controls sorted by Control Family.
    :return: the control families dictionary with the parts sorted.
    """
    for family, control in families.items():
        """"""
        for control_id, parts in control.items():
            families[family][control_id] = {
                key: value for key, value in sorted(parts.items())
            }

    return families


def sort_controls(families: dict) -> dict:
    """
    Sort the Control Parts so that they are ordered alphabetically.

    :param families: a dictionary of Controls sorted by Control Family.
    :return: the control families dictionary with the parts sorted.
    """
    for family, control in families.items():
        families[family] = {key: value for key, value in sorted(control.items())}

    return families


@click.command()
@click.option(
    "--components",
    "-c",
    "components_dir",
    required=False,
    default="components/",
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
    help="Rendered components directory",
)
@click.option(
    "--out",
    "-o",
    "output_dir",
    type=click.Path(exists=False, dir_okay=True, readable=True),
    default="docs/",
    help="Output directory (default: docs/)",
)
def main(components_dir: str, output_dir: str):
    out_dir = Path(output_dir).joinpath("sop")
    config = load_template_args()

    rendered_components = Path(components_dir)

    families = aggregate_control_data(rendered_components)

    write_files(families, out_dir, config)
    hashes.write_changes()
    print(f"Detected changes in {hashes.changed_files} files.")


if __name__ == "__main__":
    main()
