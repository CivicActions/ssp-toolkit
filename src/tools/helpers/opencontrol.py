"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-flask#license.

This module provides classes to read, write, and create
OpenControl repositories.
"""

from enum import Enum
from pathlib import Path
from typing import Any, cast

import rtyaml  # type: ignore[import-untyped]
from blinker import signal
from pydantic import BaseModel, Field, PrivateAttr, ValidationError
from slugify import slugify

OPENCONTROL_SCHEMA_VERSION = "1.0.0"
COMPONENT_SCHEMA_VERSION = "3.1.0"

FILE_SIGNAL = signal("opencontrol_file_operation")


class OpenControlElement(BaseModel):
    def new_relative_path(self):
        assert False

    def storage_path(self, root_dir=None):
        if hasattr(self, "_file"):
            p = Path(self._file)
        else:
            p = self.new_relative_path()
        if root_dir:
            return root_dir / p
        else:
            return p


class Reference(OpenControlElement):
    name: str
    path: str  # TODO (url?)
    type: str  # TODO (enum)


class Statement(OpenControlElement):
    text: str
    key: str | None


class Parameter(OpenControlElement):
    key: str
    text: str


class ImplementationStatusEnum(str, Enum):
    partial = "partial"
    complete = "complete"
    planned = "planned"
    none = "none"


class CoveredBy(OpenControlElement):
    verification_key: str
    system_key: str | None = None
    component_key: str | None = None


class Control(OpenControlElement):
    control_key: str
    standard_key: str
    covered_by: list[CoveredBy] | None = Field(default=[])
    narrative: list[Statement] = Field(default=[])
    references: list[Reference] | None = Field(default=[])
    implementation_statuses: set[ImplementationStatusEnum] | None = Field(default=None)
    control_origins: list[str] | None = Field(default=[])
    parameters: list[Parameter] | None = Field(default=[])
    _file: str = PrivateAttr()

    def get_narratives(self):
        for narrative in self.narrative:
            yield narrative


class Metadata(OpenControlElement):
    description: str | None = Field(default=None)
    maintainers: list[str] | None = Field(default=[])


class Verification(OpenControlElement):
    key: str
    name: str
    type: str
    path: str | None = Field(default=None)
    description: str | None = Field(default=None)
    test_passed: bool | None = Field(default=None)
    last_run: Any  # optional (because of Any)


class Component(OpenControlElement):
    schema_version: str = COMPONENT_SCHEMA_VERSION
    name: str
    key: str | None = Field(default=None)
    system: str | None = Field(default=None)
    documentation_complete: bool | None = Field(default=None)
    responsible_role: str | None = Field(default=None)
    references: list[Reference] | None = Field(default=[])
    verifications: list[Verification] | None = Field(default=[])
    satisfies: list[Control] = Field(default=[])

    _file: str = PrivateAttr()

    def new_relative_path(self):
        return Path("components") / Path(self.name) / Path("component.yaml")

    def get_controls(self):
        for control in self.satisfies:
            yield control


class StandardControl(OpenControlElement):
    family: str
    name: str
    description: str


class Standard(OpenControlElement):
    name: str
    license: str | None = None
    source: str | None = None
    controls: dict[str, StandardControl]
    _file: str = PrivateAttr()

    def new_relative_path(self):
        return Path("standards") / Path(slugify(self.name)).with_suffix(".yaml")


class Certification(OpenControlElement):
    name: str
    standards: dict[str, dict[str, dict]]
    _file: str = PrivateAttr()

    def standard_keys(self):
        return set(self.standards.keys())

    def controls(self, standard):
        return set(self.standards[standard].keys())

    def new_relative_path(self):
        return Path("certifications") / Path(slugify(self.name)).with_suffix(".yaml")


class System(OpenControlElement):
    pass


class Dependency(OpenControlElement):
    url: str
    revision: str
    contextdir: str | None = Field(default=None)


class Dependencies(OpenControlElement):
    certifications: list[Dependency] | None = Field(default=[])
    standards: list[Dependency] | None = Field(default=[])
    systems: list[Dependency] | None = Field(default=[])


class OpenControl(OpenControlElement):
    """
    Container for OpenControl repository.
    """

    schema_version: str = OPENCONTROL_SCHEMA_VERSION
    name: str
    metadata: Metadata | None = None
    components: list[str | Component] = Field(default=[])
    standards: list[str] | dict[str, Standard] = Field(default=[])
    certifications: list[str | Certification] = Field(default=[])
    dependencies: Dependencies | None = None

    _root_dir: str = PrivateAttr()

    def new_relative_path(self):
        return Path("opencontrol.yaml")

    def get_components(self) -> list:
        return self.components

    @classmethod
    def debug_file(cls, sender, **kwargs):
        print(
            "Loading file" if kwargs["operation"] == "read" else "Writing file",
            kwargs["path"],
        )

    @classmethod
    def load(cls, path: str | Path, debug=True):
        """
        Load an OpenControl repository from a path to the
        `opencontrol.yaml` file.
        """

        p = Path(path) if isinstance(path, str) else path
        if debug:
            FILE_SIGNAL.connect(OpenControl.debug_file)

        with p.open() as f:
            FILE_SIGNAL.send(cls, operation="read", path=p)
            root = rtyaml.load(f)
            try:
                return cls(**root)
            except ValidationError as error:
                raise error

    def save(self):
        """Write back an OpenControl repo to where it was loaded"""
        root_dir = self._root_dir
        root = self.model_dump(exclude={"standards", "components"})
        certifications = cast(
            list[Certification],
            [cert for cert in self.certifications if isinstance(cert, Certification)],
        )
        standards = (
            cast(dict[str, Standard], self.standards).values()
            if isinstance(self.standards, dict)
            else []
        )
        components = cast(
            list[Component],
            [
                component
                for component in self.components
                if isinstance(component, Component)
            ],
        )
        root["certifications"] = [
            str(cert.storage_path(root_dir)) for cert in certifications
        ]
        root["standards"] = [str(std.storage_path(root_dir)) for std in standards]
        root["components"] = [str(c.storage_path(root_dir)) for c in components]
        print(rtyaml.dump(root))

    def save_as(self, base_dir):
        """Save an OpenControl repo in a new location"""
        root = self.model_dump(exclude={"standards", "components"})
        certifications = cast(
            list[Certification],
            [cert for cert in self.certifications if isinstance(cert, Certification)],
        )
        standards = (
            list(cast(dict[str, Standard], self.standards).values())
            if isinstance(self.standards, dict)
            else []
        )
        components = cast(
            list[Component],
            [
                component
                for component in self.components
                if isinstance(component, Component)
            ],
        )
        root["certifications"] = []
        for cert in certifications:
            cert_storage = cert.storage_path(base_dir)
            cert_storage.parent.mkdir(parents=True, exist_ok=True)
            with cert_storage.open("w") as cert_file:
                cert_file.write(rtyaml.dump(cert.dict()))
                FILE_SIGNAL.send(self, operation="write", path=cert_storage)
                root["certifications"].append(str(cert.storage_path()))

        root["standards"] = []
        for std in standards:
            std_storage = std.storage_path(base_dir)
            std_storage.parent.mkdir(parents=True, exist_ok=True)
            with std_storage.open("w") as std_file:
                std_file.write(rtyaml.dump(std.dict()))
                FILE_SIGNAL.send(self, operation="write", path=std_storage)
                root["standards"].append(str(std.storage_path()))

        root["components"] = [str(c.storage_path()) for c in components]

        root_storage = self.storage_path(base_dir)
        with root_storage.open("w") as root_file:
            root_file.write(rtyaml.dump(root))
            FILE_SIGNAL.send(self, operation="write", path=root_storage)

        for c in components:
            component_path = c.storage_path(base_dir)
            component_path.parent.mkdir(parents=True, exist_ok=True)

            with component_path.open("w") as component_file:
                component_file.write(rtyaml.dump(c.dict()))
            FILE_SIGNAL.send(self, operation="write", path=component_path)


class FenComponent(BaseModel):
    schema_version: str
    name: str
    satisfies: list[str] | None = Field(default=[])


class FenFamily(BaseModel):
    schema_version: str | None = None
    family: str
    satisfies: list[Control]


class OpenControlYaml(BaseModel):
    schema_version: str
    name: str
    metadata: Metadata | None = None
    components: list[str] | None = Field(default=[])
    certifications: list[str] = Field(default=[])
    standards: list[str] = Field(default=[])
    systems: list[str] | None = None
    dependencies: dict[str, list[Dependency]] | None

    @staticmethod
    def _component_path(component, relative_to):
        path = relative_to / component
        if path.is_dir():
            path = path / "component.yaml"
        return path

    def resolve(self, relative_to):
        resolved_components = self.resolve_components(relative_to)
        resolved_certifications = self.resolve_certifications(relative_to)
        resolved_standards = self.resolve_standards(relative_to)
        obj = OpenControl.model_validate(
            {
                "schema_version": self.schema_version,
                "name": self.name,
                "metadata": self.metadata,
                "components": resolved_components,
                "certifications": resolved_certifications,
                "standards": resolved_standards,
            }
        )
        return obj

    def resolve_components(self, relative_to):
        resolved_components = []
        for component in self.components:  # type: ignore[union-attr]
            component_path = self._component_path(component, relative_to)
            if component_path.is_file():
                component = self.resolve_component(component_path)
                component._file = component_path.relative_to(relative_to)
                resolved_components.append(component)
            else:
                msg = f"Can't open component file '{component_path}'"
                raise Exception(msg)
        return resolved_components

    @staticmethod
    def _is_fen(obj):
        satisfies = obj.get("satisfies", [])
        if isinstance(satisfies, list) and len(satisfies) > 0:
            return isinstance(satisfies[0], str)
        return False

    def resolve_fen_component(self, obj, component_path):
        fc = FenComponent.model_validate(obj)
        resolved_satisfiers = []
        for satisfier in fc.satisfies or []:
            satisfier_path = component_path.parent / satisfier
            if satisfier_path.is_file():
                FILE_SIGNAL.send(self, operation="read", path=satisfier_path)
                with satisfier_path.open() as f:
                    obj = rtyaml.load(f)
                    family = FenFamily.model_validate(obj)
                    for satisfaction in family.satisfies:
                        satisfaction._file = satisfier_path
                        resolved_satisfiers.append(satisfaction)

        c = Component(
            schema_version=fc.schema_version,
            name=fc.name,
            satisfies=resolved_satisfiers,
        )
        return c

    def resolve_component(self, component_path):
        FILE_SIGNAL.send(self, operation="read", path=component_path)
        with component_path.open() as f:
            obj = rtyaml.load(f)
            if self._is_fen(obj):
                return self.resolve_fen_component(obj, component_path)
            else:
                comp = Component.model_validate(obj)
            return comp

    def resolve_certifications(self, relative_to):
        certifications = []
        for certification in self.certifications:
            certification_path = relative_to / certification
            if certification_path.is_file():
                FILE_SIGNAL.send(self, operation="read", path=certification_path)
                with certification_path.open() as f:
                    obj = rtyaml.load(f)
                    cert = Certification.model_validate(obj)
                    cert._file = certification
                    certifications.append(cert)
            else:
                msg = f"Can't open certification file '{certification_path}'"
                raise Exception(msg)
        return certifications

    def resolve_standards(self, relative_to):
        standards = {}
        for standard in self.standards:
            standard_path = relative_to / standard
            if standard_path.is_file():
                FILE_SIGNAL.send(self, operation="read", path=standard_path)
                with standard_path.open() as f:
                    obj = rtyaml.load(f)
                    name = obj.pop("name")

                    # TODO: source and license are not in the spec?

                    source = obj.pop("source", "")
                    license = obj.pop("license", "")

                    controls = {
                        control: StandardControl.model_validate(desc)
                        for control, desc in obj.items()
                        if "family" in desc
                    }

                    std = Standard(
                        name=name, controls=controls, source=source, license=license
                    )
                    std._file = standard
                    standards[name] = std
            else:
                raise Exception(f"Can't open standard file '{standard_path}'")
        return standards

    def resolve_dependencies(self, relative_to):
        pass


def load(f, debug=False):
    return OpenControl.load(f, debug)
