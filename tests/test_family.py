"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

from collections import OrderedDict

from tools.helpers.family import Control, Family, Part, sort_by_keys


class TestSortByKeys:
    def test_returns_sorted_ordered_dict(self):
        result = sort_by_keys({"b": 2, "a": 1, "c": 3})
        assert isinstance(result, OrderedDict)
        assert list(result.keys()) == ["a", "b", "c"]

    def test_empty_dict(self):
        assert sort_by_keys({}) == OrderedDict()

    def test_already_sorted(self):
        result = sort_by_keys({"a": 1, "b": 2})
        assert list(result.keys()) == ["a", "b"]


class TestPart:
    def setup_method(self):
        self.part = Part(key="a", party="System Owner", narrative="We do the thing.")

    def test_str_includes_party(self):
        text = str(self.part)
        assert "System Owner" in text

    def test_str_includes_narrative(self):
        text = str(self.part)
        assert "We do the thing." in text

    def test_str_format(self):
        text = str(self.part)
        assert text == "##### System Owner\n\nWe do the thing.\n"


class TestControl:
    def setup_method(self):
        self.control = Control(
            control_id="AC-1",
            control_name="Policy and Procedures",
            description="Develop and implement access control policy.",
            status="complete",
            parts={},
            control_type="Hybrid",
        )

    def test_header_contains_control_id(self):
        assert "AC-1" in self.control.header()

    def test_header_contains_control_name(self):
        assert "Policy and Procedures" in self.control.header()

    def test_control_description_in_code_block(self):
        desc = self.control.control_description()
        assert "```text" in desc
        assert "Develop and implement access control policy." in desc
        assert "```" in desc

    def test_get_status_contains_status(self):
        assert "complete" in self.control.get_status()

    def test_get_status_format(self):
        assert self.control.get_status() == "**Status:** complete\n"

    def test_str_combines_all_sections(self):
        text = str(self.control)
        assert "AC-1" in text
        assert "Policy and Procedures" in text
        assert "complete" in text

    def test_add_part_creates_new_list(self):
        part = Part(key="a", party="Owner", narrative="Narrative text.")
        self.control.add_part("a", part)
        assert "a" in self.control.parts
        assert len(self.control.parts["a"]) == 1

    def test_add_part_appends_to_existing_key(self):
        part1 = Part(key="a", party="Owner1", narrative="First.")
        part2 = Part(key="a", party="Owner2", narrative="Second.")
        self.control.add_part("a", part1)
        self.control.add_part("a", part2)
        assert len(self.control.parts["a"]) == 2

    def test_get_parts_default_key_has_no_header(self):
        part = Part(key="_default", party="Owner", narrative="Some narrative.")
        self.control.add_part("_default", part)
        parts_text = self.control.get_parts()
        assert "#### _default" not in parts_text
        assert "Some narrative." in parts_text

    def test_get_parts_named_key_has_header(self):
        part = Part(key="a", party="Owner", narrative="Part a narrative.")
        self.control.add_part("a", part)
        parts_text = self.control.get_parts()
        assert "#### a" in parts_text

    def test_get_parts_sorted_by_key(self):
        part_b = Part(key="b", party="Owner", narrative="B narrative.")
        part_a = Part(key="a", party="Owner", narrative="A narrative.")
        self.control.add_part("b", part_b)
        self.control.add_part("a", part_a)
        parts_text = self.control.get_parts()
        assert parts_text.index("#### a") < parts_text.index("#### b")


class TestFamily:
    def setup_method(self):
        self.family = Family(
            title="Test SSP",
            family_id="AC",
            family_name="Access Control",
            controls={},
        )

    def test_header_contains_title(self):
        assert "Test SSP" in self.family.header()

    def test_header_contains_family_id(self):
        assert "AC" in self.family.header()

    def test_header_contains_family_name(self):
        assert "Access Control" in self.family.header()

    def test_add_control(self):
        control = Control(
            control_id="AC-1",
            control_name="Policy",
            description="desc",
            status="complete",
            parts={},
            control_type="Hybrid",
        )
        self.family.add_control("AC-01", control)
        assert "AC-01" in self.family.controls

    def test_get_controls_empty(self):
        assert self.family.get_controls() == ""

    def test_get_controls_returns_control_text(self):
        control = Control(
            control_id="AC-1",
            control_name="Policy",
            description="desc",
            status="complete",
            parts={},
            control_type="Hybrid",
        )
        self.family.add_control("AC-01", control)
        text = self.family.get_controls()
        assert "AC-1" in text
        assert "Policy" in text

    def test_print_family_file_creates_file(self, tmp_path):
        control = Control(
            control_id="AC-1",
            control_name="Policy",
            description="desc",
            status="complete",
            parts={},
            control_type="Hybrid",
        )
        self.family.add_control("AC-01", control)
        self.family.print_family_file(out_path=tmp_path)
        output_file = tmp_path / "AC.md"
        assert output_file.exists()
        content = output_file.read_text()
        assert "AC" in content
        assert "Access Control" in content
