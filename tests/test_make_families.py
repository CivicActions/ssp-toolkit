"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import pytest

from tools.helpers.family import Control
from tools.make_families import (
    get_control_narratives,
    get_control_parts,
    get_standard_by_control_id,
    update_control_type,
    update_status,
)


def make_control(**kwargs):
    defaults = dict(
        control_id="AC-1",
        control_name="Policy",
        description="desc",
        status=None,
        parts={},
        control_type=None,
    )
    defaults.update(kwargs)
    return Control(**defaults)


class TestUpdateStatus:
    def test_sets_status_when_none(self):
        control = make_control(status=None)
        update_status(control, "complete")
        assert control.status == "complete"

    def test_upgrades_to_complete(self):
        control = make_control(status="partial")
        update_status(control, "complete")
        assert control.status == "complete"

    def test_sets_any_status(self):
        control = make_control(status="complete")
        update_status(control, "partial")
        assert control.status == "partial"


class TestUpdateControlType:
    def test_sets_control_type(self):
        control = make_control(control_type=None)
        update_control_type(control, "Hybrid")
        assert control.control_type == "Hybrid"

    def test_overwrites_existing_type(self):
        control = make_control(control_type="System")
        update_control_type(control, "Inherited")
        assert control.control_type == "Inherited"


class TestGetControlParts:
    def test_adds_parts_from_narrative(self):
        control = make_control()
        parts = [{"key": "a", "text": "Narrative for part a."}]
        result = get_control_parts(parts=parts, control=control, parent="System Owner")
        assert "a" in result.parts
        assert result.parts["a"][0].narrative == "Narrative for part a."

    def test_missing_key_uses_default(self):
        control = make_control()
        parts = [{"text": "Default part."}]
        result = get_control_parts(parts=parts, control=control, parent="Owner")
        assert "_default" in result.parts

    def test_multiple_parts_added(self):
        control = make_control()
        parts = [
            {"key": "a", "text": "Part A."},
            {"key": "b", "text": "Part B."},
        ]
        result = get_control_parts(parts=parts, control=control, parent="Owner")
        assert "a" in result.parts
        assert "b" in result.parts

    def test_returns_control(self):
        control = make_control()
        result = get_control_parts(parts=[], control=control, parent="Owner")
        assert isinstance(result, Control)


class TestGetStandardByControlId:
    def setup_method(self):
        self.standards = [
            {
                "AC-1": {"name": "Policy", "description": "..."},
                "AC-2": {"name": "Accounts"},
            },
            {"SI-1": {"name": "SI Policy"}},
        ]

    def test_finds_in_first_standard(self):
        result = get_standard_by_control_id("AC-1", self.standards)
        assert result["name"] == "Policy"

    def test_finds_in_second_standard(self):
        result = get_standard_by_control_id("SI-1", self.standards)
        assert result["name"] == "SI Policy"

    def test_raises_for_missing(self):
        with pytest.raises(KeyError, match="MISSING"):
            get_standard_by_control_id("MISSING", self.standards)


class TestGetControlNarratives:
    def test_yields_tuples(self):
        component_controls = [
            {
                "Component1": {
                    "narrative": [{"key": "a", "text": "Some text."}],
                    "implementation_status": "complete",
                    "security_control_type": "Hybrid",
                }
            }
        ]
        results = list(get_control_narratives(component_controls))
        assert len(results) == 1
        key, narrative, status, control_type = results[0]
        assert key == "Component1"
        assert narrative == [{"key": "a", "text": "Some text."}]
        assert status == "complete"
        assert control_type == "Hybrid"

    def test_handles_multiple_components(self):
        component_controls = [
            {
                "CompA": {
                    "narrative": [],
                    "implementation_status": "partial",
                    "security_control_type": None,
                }
            },
            {
                "CompB": {
                    "narrative": [],
                    "implementation_status": "complete",
                    "security_control_type": "System",
                }
            },
        ]
        results = list(get_control_narratives(component_controls))
        assert len(results) == 2
        keys = [r[0] for r in results]
        assert "CompA" in keys
        assert "CompB" in keys
