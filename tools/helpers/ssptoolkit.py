"""
Copyright 2019-2020 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/compliancetools#copyright.
"""

import re
from pathlib import Path

import yaml
from complianceio.opencontrol import OpenControl
from yamlinclude import YamlIncludeConstructor

from tools.helpers import secrender


def sortable_control_id(control_id: str) -> str:
    return re.sub(r"(\d+)", lambda m: m.group(1).zfill(2), control_id)


def get_project() -> OpenControl:
    oc_file = Path("opencontrol").with_suffix(".yaml")
    project = OpenControl.load(oc_file.as_posix())
    return project


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

    title = project.get("metadata").get("description")
    return title, standards


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

    return component_files


def load_project_data() -> OpenControl:
    oc_yaml = Path().joinpath("opencontrol.yaml")
    if not oc_yaml.is_file():
        raise FileNotFoundError
    project = OpenControl.load(path=oc_yaml.as_posix())
    return project


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
                cid = sortable_control_id(control_id=control_id)
                if cid not in controls:
                    controls[cid] = []
                controls[cid].append({parent: satisfies})

    return dict(sorted(controls.items()))


def load_template_args(config_file: str) -> dict:
    YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader)
    with open(config_file, "r", newline="") as fp:
        config = yaml.load(fp, Loader=yaml.FullLoader)
    return secrender.get_template_args(yaml=config, set_={}, root=None)