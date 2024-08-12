"""
Copyright 2019-2024 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#copyright.
"""

import mmap
import re
from pathlib import Path

import md_toc
import yaml
from complianceio.opencontrol import OpenControl
from yamlinclude import YamlIncludeConstructor

from tools.helpers import secrender


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
    oc_file = Path("opencontrol").with_suffix(".yaml")
    if oc_file.is_file():
        project = OpenControl.load(oc_file.as_posix())
    else:
        raise FileNotFoundError("Could not find opencontrol.yaml file.")
    return project


def get_certification_baseline() -> list:
    project = get_project()
    certifications: list = []
    for certs in project.certifications:
        try:
            with open(certs, "r") as s:
                certifications.append(yaml.load(s, Loader=yaml.SafeLoader))
        except FileNotFoundError as error:
            raise error

    controls: list = []
    for standards in certifications:
        for _, control_ids in standards.get("standards").items():
            controls.extend(control_ids.keys())

    return list(dict.fromkeys(controls))


def get_standards() -> tuple:
    project = get_project()
    standards: list = []
    for standard in project.standards:
        try:
            with open(standard, "r") as s:
                standards_list = yaml.load(s, Loader=yaml.SafeLoader)
        except FileNotFoundError as error:
            raise error
        standards.append(standards_list)

    title = project.metadata.description
    return title, standards


def get_standards_control_data(control: str, standards: list) -> dict:
    for s in standards:
        if control_data := s.get(control):
            return control_data
    raise KeyError(f"Control {control} not found.")


def get_standards_family_name(family: str, standards: list) -> str:
    for s in standards:
        if control_data := s.get(family, None):
            return control_data.get("name")
    raise KeyError(f"Control {family} not found.")


def get_component_files(components: list) -> dict:
    component_files: dict = {}
    for c in components:
        with open(Path(c).joinpath("component.yaml"), "r") as cfp:
            component = yaml.load(cfp, Loader=yaml.SafeLoader)
        for family in component.get("satisfies"):
            component_file = Path().joinpath(c, family)
            family_name = component_file.stem
            if family_name not in component_files:
                component_files[family_name] = []
            component_files[family_name].append(component_file.as_posix())

    return dict(sorted(component_files.items()))


def load_controls_by_id(component_list: list) -> dict:
    component_files = get_component_files(components=component_list)
    controls: dict = {}
    for _, components in component_files.items():
        for component in components:
            component_path = Path(component)
            try:
                with open(component_path, "r") as fp:
                    component_data = yaml.load(fp, Loader=yaml.SafeLoader)
            except FileNotFoundError as error:
                raise error
            parent = component_path.parents[0].name
            for satisfies in component_data.get("satisfies"):
                control_id = satisfies.get("control_key")
                cid = control_id
                if cid not in controls:
                    controls[cid] = []
                controls[cid].append({parent: satisfies})

    return dict(sorted(controls.items()))


def load_template_args() -> dict:
    YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader)
    config = load_yaml_files("configuration.yaml")
    return secrender.get_template_args(yaml=config, set_={}, root="")


def get_control_statuses() -> dict:
    p = Path("keys/status.yaml")
    try:
        with p.open("r") as fp:
            statuses = yaml.load(fp, Loader=yaml.SafeLoader)
    except FileNotFoundError as error:
        raise error
    return statuses


def find_toc_tag(file: str, levels: int = 3):
    with open(file, "rb", 0) as f, mmap.mmap(
        f.fileno(), 0, access=mmap.ACCESS_READ
    ) as s:
        if s.find(b"<!--TOC-->") != -1:
            write_toc(file, levels=levels)


def write_toc(file: str | Path, levels: int):
    toc = md_toc.api.build_toc(filename=file, keep_header_levels=levels, skip_lines=5)
    md_toc.api.write_string_on_file_between_markers(
        filename=file,
        string=toc,
        marker="<!--TOC-->",
    )


def load_yaml_files(file_path: str | Path) -> dict:
    load_file = Path(file_path) if isinstance(file_path, str) else file_path
    try:
        with open(load_file, "r") as fp:
            project = yaml.load(fp, Loader=yaml.FullLoader)
            return project
    except FileNotFoundError:
        raise FileNotFoundError(
            f"No {load_file.name} found in {load_file.parent.as_posix()}."
        )
