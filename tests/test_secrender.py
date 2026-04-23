"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

from tools.helpers.secrender import get_template, get_template_args, make_output_path


class TestGetTemplateArgs:
    def test_returns_all_yaml_keys(self):
        yaml_data = {"key1": "value1", "key2": "value2"}
        result = get_template_args(yaml=yaml_data, set_={})
        assert result["key1"] == "value1"
        assert result["key2"] == "value2"

    def test_includes_current_date(self):
        result = get_template_args(yaml={}, set_={})
        assert "current_date" in result

    def test_set_overrides_values(self):
        yaml_data = {"key": "from_yaml"}
        set_data = {"key": "from_set"}
        result = get_template_args(yaml=yaml_data, set_=set_data)
        assert result["key"] == "from_set"

    def test_set_adds_new_keys(self):
        result = get_template_args(yaml={}, set_={"extra": "added"})
        assert result["extra"] == "added"

    def test_root_wraps_yaml_in_namespace(self):
        yaml_data = {"name": "test"}
        result = get_template_args(yaml=yaml_data, set_={}, root="ssp")
        assert "ssp" in result
        assert result["ssp"]["name"] == "test"
        assert "name" not in result

    def test_empty_root_no_namespace(self):
        yaml_data = {"name": "test"}
        result = get_template_args(yaml=yaml_data, set_={}, root="")
        assert result["name"] == "test"

    def test_root_does_not_affect_set_keys(self):
        yaml_data = {"key": "value"}
        set_data = {"extra": "value"}
        result = get_template_args(yaml=yaml_data, set_=set_data, root="namespace")
        assert result["extra"] == "value"
        assert "namespace" in result
        assert result["namespace"]["key"] == "value"


class TestMakeOutputPath:
    def test_stdout_alias(self):
        result = make_output_path("-", "/some/dir")
        assert result == "/dev/stdout"

    def test_absolute_path_returned_unchanged(self):
        result = make_output_path("/absolute/path/out.md", "/ignored/dir")
        assert result == "/absolute/path/out.md"

    def test_relative_path_joined_with_output_dir(self):
        result = make_output_path("output.md", "/base/dir")
        assert result == "/base/dir/output.md"

    def test_none_output_dir_returns_relative(self):
        result = make_output_path("output.md", None)
        assert result == "output.md"


class TestGetTemplate:
    def test_loads_template(self, tmp_path):
        template_file = tmp_path / "test.j2"
        template_file.write_text("Hello, {{ name }}!")
        template = get_template(str(template_file))
        assert template.render(name="World") == "Hello, World!"

    def test_template_with_loop(self, tmp_path):
        template_file = tmp_path / "list.j2"
        template_file.write_text("{% for item in items %}{{ item }}\n{% endfor %}")
        template = get_template(str(template_file))
        rendered = template.render(items=["a", "b", "c"])
        assert "a" in rendered
        assert "b" in rendered
        assert "c" in rendered
