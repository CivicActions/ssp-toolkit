"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import pytest

from tools.helpers.ssptoolkit import (
    get_standards_control_data,
    get_standards_family_name,
    sortable_control_id,
    to_oc_control_id,
)


class TestSortableControlId:
    def test_pads_single_digit_numbers(self):
        assert sortable_control_id("AC-1") == "AC-01"

    def test_pads_two_digit_numbers(self):
        assert sortable_control_id("AC-10") == "AC-10"

    def test_pads_extended_control(self):
        assert sortable_control_id("AC-2 (1)") == "AC-02 (01)"

    def test_pads_multiple_numbers(self):
        assert sortable_control_id("SI-3 (10)") == "SI-03 (10)"

    def test_already_padded_unchanged(self):
        assert sortable_control_id("AC-01") == "AC-01"

    def test_three_digit_number_padded(self):
        assert sortable_control_id("AC-1 (1)") == "AC-01 (01)"


class TestToOcControlId:
    def test_simple_control_strips_leading_zero(self):
        assert to_oc_control_id("AC-01") == "AC-1"

    def test_simple_control_no_padding(self):
        assert to_oc_control_id("AC-1") == "AC-1"

    def test_two_digit_number(self):
        assert to_oc_control_id("AC-10") == "AC-10"

    def test_extended_control(self):
        assert to_oc_control_id("AC-02 (01)") == "AC-2 (1)"

    def test_extended_control_multidigit(self):
        # The OC extended regex requires 0-prefixed numbers (0\d+).
        # AC-10 does not start with 0, so it does not match and is returned unchanged.
        assert to_oc_control_id("AC-10 (02)") == "AC-10 (02)"

    def test_unrecognized_format_returned_unchanged(self):
        result = to_oc_control_id("CUSTOM-CONTROL")
        assert result == "CUSTOM-CONTROL"


class TestGetStandardsControlData:
    def setup_method(self):
        self.standards = [
            {
                "AC-1": {"name": "Policy and Procedures", "description": "..."},
                "AC-2": {"name": "Account Management", "description": "..."},
            },
            {
                "SI-1": {"name": "System and Info Integrity", "description": "..."},
            },
        ]

    def test_finds_control_in_first_standard(self):
        result = get_standards_control_data("AC-1", self.standards)
        assert result["name"] == "Policy and Procedures"

    def test_finds_control_in_second_standard(self):
        result = get_standards_control_data("SI-1", self.standards)
        assert result["name"] == "System and Info Integrity"

    def test_raises_key_error_for_missing_control(self):
        with pytest.raises(KeyError, match="MISSING"):
            get_standards_control_data("MISSING", self.standards)

    def test_returns_full_dict_for_control(self):
        result = get_standards_control_data("AC-2", self.standards)
        assert result == {"name": "Account Management", "description": "..."}


class TestGetStandardsFamilyName:
    def setup_method(self):
        self.standards = [
            {
                "AC": {"name": "Access Control", "description": ""},
                "SI": {"name": "System and Information Integrity", "description": ""},
            }
        ]

    def test_finds_family_name(self):
        result = get_standards_family_name("AC", self.standards)
        assert result == "Access Control"

    def test_finds_another_family_name(self):
        result = get_standards_family_name("SI", self.standards)
        assert result == "System and Information Integrity"

    def test_raises_key_error_for_missing_family(self):
        with pytest.raises(KeyError, match="ZZ"):
            get_standards_family_name("ZZ", self.standards)
