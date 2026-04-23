"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

from pathlib import Path
from typing import Generator

from tools.helpers.helpers import get_project_path, load_yaml_files
from tools.helpers.opencontrol import OpenControl
from tools.helpers.ssptoolkit import get_project, sortable_control_id


class Project:
    project: OpenControl
    project_path: Path
    config: str
    controls: dict

    def __init__(self):
        self.project = get_project()
        self.project_path = get_project_path()
        if self.project_path.joinpath("configuration.yaml").exists():
            self.config = "configuration.yaml"
        else:
            raise FileNotFoundError("configuration.yaml not found in project root.")
        self._sort_standard_controls()

    def _sort_standard_controls(self) -> None:
        controls: dict[str, dict[str, str]] = {}
        for certification in self.project.certifications:
            if not isinstance(certification, str):
                continue
            cert_path = self.project_path.joinpath(certification)
            cert = load_yaml_files(cert_path)

            for control in self._get_certification_controls(cert):
                family = control[:2]
                if family not in controls:
                    controls[family] = {}
                controls[family][sortable_control_id(control)] = control
                controls[family] = {
                    key: value for key, value in sorted(controls[family].items())
                }
        self.controls = dict(sorted(controls.items()))

    @staticmethod
    def _get_certification_controls(cert: dict) -> Generator[str, None, None]:
        for standard in cert.get("standards", {}).values():
            for control_id, _ in standard.items():
                yield control_id

    def get_standards(self) -> tuple:
        standards: list = []
        self.project_path = get_project_path()
        for standard in self.project.standards:
            standards_list = load_yaml_files(self.project_path / standard)
            standards.append(standards_list)

        title = (
            self.project.metadata.description
            if self.project.metadata and self.project.metadata.description
            else ""
        )
        return title, standards

    def sort_component_controls(self, component_name: str) -> dict:
        controls: dict = {}
        for component_dir in self.project.components:
            if not isinstance(component_dir, str):
                continue
            component_path = (
                Path(component_dir).joinpath(component_name).with_suffix(".yaml")
            )

            if component_path.exists():
                component_data = load_yaml_files(component_path)
                for control_id, narrative in self._get_control_narratives(
                    component_data
                ):
                    if control_id not in controls:
                        controls[control_id] = []
                    controls[control_id].append({component_path.parent.name: narrative})
        return controls

    @staticmethod
    def _get_control_narratives(component: dict) -> Generator[tuple, None, None]:
        for satisfies in component.get("satisfies", []):
            scid = sortable_control_id(satisfies.get("control_key"))
            yield scid, satisfies
