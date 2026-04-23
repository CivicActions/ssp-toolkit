"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import mmap
import re
from pathlib import Path

import md_toc  # type: ignore[import-untyped]
import yaml
from loguru import logger

from tools.config import Config
from tools.helpers import secrender
from tools.helpers.helpers import get_project_path, load_yaml_files
from tools.helpers.opencontrol import OpenControl
from tools.logging_config import setup_logging  # noqa: F401


class ControlRegExps:
    oc_simple = re.compile(r"^([A-Z]{2})-(0\d+)$")
    oc_extended = re.compile(r"^([A-Z]{2})-(0\d+)\s*\((0\d+)\)$")


def sortable_control_id(control_id: str) -> str:
    return re.sub(r"(\d+)", lambda m: m.group(1).zfill(2), control_id)


def to_oc_control_id(control_id: str) -> str:
    match = re.match(ControlRegExps.oc_simple, control_id)
    if match:
        family = match.group(1)
        number = int(match.group(2))
        return f"{family}-{number}"

    # AC-2(1)
    match = re.match(ControlRegExps.oc_extended, control_id)
    if match:
        family = match.group(1)
        number = int(match.group(2))
        extension = int(match.group(3))
        return f"{family}-{number} ({extension})"

    return control_id


def get_project() -> OpenControl:
    project_path = get_project_path()
    oc_file = project_path.joinpath("opencontrol").with_suffix(".yaml")
    if oc_file.is_file():
        project = OpenControl.load(oc_file.as_posix())
    else:
        logger.error(f"OpenControl file not found in {project_path.as_posix()}.")
        raise FileNotFoundError(
            "Could not find opencontrol.yaml file in {project_path.as_posix()}."
        )
    return project


def get_certification_baseline() -> list:
    project = get_project()
    project_path = get_project_path()
    certifications: list = []
    for certs in project.certifications:
        if isinstance(certs, str):
            certifications.append(load_yaml_files(project_path / certs))

    controls: list = []
    for standards in certifications:
        for _, control_ids in standards.get("standards").items():
            controls.extend(control_ids.keys())

    return list(dict.fromkeys(controls))


def get_standards() -> tuple:
    project = get_project()
    standards: list = []
    for standard in project.standards:
        if isinstance(standard, str):
            try:
                with open(standard, "r") as s:
                    standards_list = yaml.load(s, Loader=yaml.SafeLoader)
            except FileNotFoundError as error:
                raise error
            standards.append(standards_list)

    title = (
        project.metadata.description
        if project.metadata and project.metadata.description
        else ""
    )
    return title, standards


def get_standards_control_data(control: str, standards: list) -> dict:
    for standard in standards:
        if control_data := standard.get(control):
            return control_data
    logger.error(f"Control {control} not found.")
    raise KeyError(f"Control {control} not found.")


def get_standards_family_name(family: str, standards: list) -> str:
    for standard in standards:
        if control_data := standard.get(family, None):
            return control_data.get("name")
    logger.error(f"Control {family} not found.")
    raise KeyError(f"Control {family} not found.")


def get_component_files(components: list) -> dict:
    component_files: dict = {}
    project_path = get_project_path()
    for component_path in components:
        component = load_yaml_files(
            project_path / "rendered" / component_path / "component.yaml"
        )
        for family in component.get("satisfies", {}):
            component_family = project_path / "rendered" / component_path / family
            family_name = component_family.stem
            if family_name not in component_files:
                component_files[family_name] = []
            component_files[family_name].append(component_family.as_posix())

    return dict(sorted(component_files.items()))


def load_controls_by_id(component_list: list) -> dict:
    component_files = get_component_files(components=component_list)
    controls: dict = {}
    for _, components in component_files.items():
        for component in components:
            component_path = Path(component)
            component_data = load_yaml_files(component_path)
            parent = component_path.parent.name

            for satisfies in component_data.get("satisfies", {}):
                control_id = satisfies.get("control_key")
                cid = control_id
                if cid not in controls:
                    controls[cid] = []
                controls[cid].append({parent: satisfies})

    return dict(sorted(controls.items()))


def load_template_args() -> dict:
    config = Config()
    return secrender.get_template_args(yaml=config.config, set_={}, root="")


def get_control_statuses() -> dict:
    config = Config()
    statuses = config.config.get("status", {})
    return statuses


def find_toc_tag(file: str, levels: int = 3):
    with (
        open(file, "rb", 0) as f,
        mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as s,
    ):
        if s.find(b"<!--TOC-->") != -1:
            write_toc(file, levels=levels)


def write_toc(file: str | Path, levels: int):
    filename = str(file)
    toc = md_toc.api.build_toc(
        filename=filename, keep_header_levels=levels, skip_lines=5
    )
    md_toc.api.write_string_on_file_between_markers(
        filename=filename,
        string=toc,
        marker="<!--TOC-->",
    )
