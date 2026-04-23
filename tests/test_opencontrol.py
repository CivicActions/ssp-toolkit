"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import pytest
from pydantic import ValidationError

from tools.helpers.opencontrol import (
    Certification,
    Component,
    Control,
    CoveredBy,
    ImplementationStatusEnum,
    Metadata,
    OpenControl,
    Parameter,
    Statement,
    Verification,
)


class TestStatement:
    def test_valid_statement(self):
        s = Statement(text="Some narrative.", key="a")
        assert s.text == "Some narrative."
        assert s.key == "a"

    def test_key_optional(self):
        s = Statement(text="No key.", key=None)
        assert s.key is None


class TestParameter:
    def test_valid_parameter(self):
        p = Parameter(key="param1", text="Value one")
        assert p.key == "param1"
        assert p.text == "Value one"


class TestImplementationStatusEnum:
    def test_valid_values(self):
        assert ImplementationStatusEnum.partial == "partial"
        assert ImplementationStatusEnum.complete == "complete"
        assert ImplementationStatusEnum.planned == "planned"
        assert ImplementationStatusEnum.none == "none"


class TestCoveredBy:
    def test_required_field(self):
        cb = CoveredBy(verification_key="vk1")
        assert cb.verification_key == "vk1"
        assert cb.system_key is None
        assert cb.component_key is None


class TestControl:
    def test_minimal_control(self):
        control = Control(control_key="AC-1", standard_key="NIST 800-53")
        assert control.control_key == "AC-1"
        assert control.standard_key == "NIST 800-53"
        assert control.narrative == []
        assert control.covered_by == []

    def test_control_with_narratives(self):
        control = Control(
            control_key="AC-1",
            standard_key="NIST 800-53",
            narrative=[Statement(text="We do this.", key="a")],
        )
        narratives = list(control.get_narratives())
        assert len(narratives) == 1
        assert narratives[0].text == "We do this."

    def test_implementation_status_enum(self):
        control = Control(
            control_key="AC-1",
            standard_key="NIST 800-53",
            implementation_statuses={ImplementationStatusEnum.complete},
        )
        assert ImplementationStatusEnum.complete in control.implementation_statuses


class TestMetadata:
    def test_all_optional(self):
        m = Metadata()
        assert m.description is None
        assert m.maintainers == []

    def test_with_values(self):
        m = Metadata(description="Test project", maintainers=["Alice", "Bob"])
        assert m.description == "Test project"
        assert "Alice" in m.maintainers


class TestVerification:
    def test_required_fields(self):
        v = Verification(key="v1", name="Test Check", type="test", last_run=None)
        assert v.key == "v1"
        assert v.test_passed is None

    def test_optional_fields_default_to_none(self):
        v = Verification(
            key="v1", name="Test Check", type="test", last_run="2024-01-01"
        )
        assert v.path is None
        assert v.description is None


class TestComponent:
    def test_minimal_component(self):
        comp = Component(name="TestComponent")
        assert comp.name == "TestComponent"
        assert comp.satisfies == []

    def test_component_with_controls(self):
        control = Control(control_key="AC-1", standard_key="NIST 800-53")
        comp = Component(name="TestComponent", satisfies=[control])
        controls = list(comp.get_controls())
        assert len(controls) == 1
        assert controls[0].control_key == "AC-1"

    def test_new_relative_path(self):
        comp = Component(name="TestComponent")
        path = comp.new_relative_path()
        assert "TestComponent" in str(path)
        assert path.suffix == ".yaml"


class TestCertification:
    def setup_method(self):
        self.cert = Certification(
            name="FISMA Low",
            standards={
                "NIST SP 800-53": {
                    "AC-1": {},
                    "AC-2": {},
                    "SI-1": {},
                }
            },
        )

    def test_standard_keys(self):
        keys = self.cert.standard_keys()
        assert "NIST SP 800-53" in keys

    def test_controls_for_standard(self):
        controls = self.cert.controls("NIST SP 800-53")
        assert "AC-1" in controls
        assert "AC-2" in controls
        assert "SI-1" in controls

    def test_new_relative_path(self):
        path = self.cert.new_relative_path()
        assert "certifications" in str(path)
        assert path.suffix == ".yaml"


class TestOpenControl:
    def test_minimal_opencontrol(self):
        oc = OpenControl(name="Test Project", metadata=Metadata())
        assert oc.name == "Test Project"
        assert oc.components == []
        assert oc.standards == []
        assert oc.certifications == []

    def test_get_components(self):
        oc = OpenControl(
            name="Test Project",
            metadata=Metadata(),
            components=["./components/A", "./components/B"],
        )
        assert len(oc.get_components()) == 2

    def test_load_from_file(self, project_env):
        oc_file = project_env / "opencontrol.yaml"
        oc = OpenControl.load(oc_file, debug=False)
        assert oc.name == "Test Project"
        assert len(oc.components) > 0

    def test_missing_required_field_raises(self):
        with pytest.raises(ValidationError):
            OpenControl(metadata=Metadata())
