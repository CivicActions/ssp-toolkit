"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import pytest
from ruamel.yaml import YAMLError

from tools.helpers.helpers import (
    cached_file_loader,
    get_hash,
    get_project_path,
    load_yaml_files,
    write_files,
    write_yaml_files,
)


class TestGetProjectPath:
    def test_returns_path_when_valid(self, project_env):
        path = get_project_path()
        assert path == project_env

    def test_raises_when_env_not_set(self, monkeypatch):
        monkeypatch.delenv("PROJECT_PATH", raising=False)
        with pytest.raises(ValueError, match="PROJECT_PATH"):
            get_project_path()

    def test_raises_when_no_opencontrol_yaml(self, tmp_path, monkeypatch):
        monkeypatch.setenv("PROJECT_PATH", str(tmp_path))
        with pytest.raises(FileNotFoundError, match="opencontrol.yaml"):
            get_project_path()


class TestLoadYamlFiles:
    def test_loads_valid_yaml(self, tmp_path):
        yaml_file = tmp_path / "test.yaml"
        yaml_file.write_text("key: value\nnumber: 42\n")
        result = load_yaml_files(yaml_file)
        assert result == {"key": "value", "number": 42}

    def test_returns_empty_dict_on_missing_file(self, tmp_path):
        result = load_yaml_files(tmp_path / "nonexistent.yaml")
        assert result == {}

    def test_returns_empty_dict_on_invalid_yaml(self, tmp_path):
        yaml_file = tmp_path / "bad.yaml"
        yaml_file.write_text("key: [unclosed bracket\n")
        result = load_yaml_files(yaml_file)
        assert result == {}

    def test_accepts_string_path(self, tmp_path):
        yaml_file = tmp_path / "test.yaml"
        yaml_file.write_text("foo: bar\n")
        result = load_yaml_files(str(yaml_file))
        assert result == {"foo": "bar"}

    def test_loads_nested_yaml(self, tmp_path):
        yaml_file = tmp_path / "nested.yaml"
        yaml_file.write_text("outer:\n  inner: value\n  list:\n    - a\n    - b\n")
        result = load_yaml_files(yaml_file)
        assert result["outer"]["inner"] == "value"
        assert result["outer"]["list"] == ["a", "b"]


class TestWriteYamlFiles:
    def test_writes_yaml_file(self, tmp_path):
        yaml_file = tmp_path / "output.yaml"
        content = {"key": "value", "number": 42}
        write_yaml_files(yaml_file, content)
        assert yaml_file.exists()
        result = load_yaml_files(yaml_file)
        assert result["key"] == "value"
        assert result["number"] == 42

    def test_raises_on_wrong_extension(self, tmp_path):
        bad_file = tmp_path / "output.txt"
        with pytest.raises(YAMLError):
            write_yaml_files(bad_file, {"key": "value"})

    def test_raises_when_parent_dir_missing(self, tmp_path):
        missing_parent = tmp_path / "missing" / "output.yaml"
        with pytest.raises(YAMLError):
            write_yaml_files(missing_parent, {"key": "value"})

    def test_accepts_string_path(self, tmp_path):
        yaml_file = tmp_path / "output.yaml"
        write_yaml_files(str(yaml_file), {"key": "value"})
        assert yaml_file.exists()


class TestWriteFiles:
    def test_writes_text_file(self, tmp_path):
        output = tmp_path / "output.txt"
        write_files(output, "Hello, world!")
        assert output.read_text() == "Hello, world!"

    def test_creates_parent_directories(self, tmp_path):
        nested = tmp_path / "a" / "b" / "c" / "output.txt"
        write_files(nested, "content")
        assert nested.exists()
        assert nested.read_text() == "content"

    def test_overwrites_existing_file(self, tmp_path):
        output = tmp_path / "output.txt"
        output.write_text("old content")
        write_files(output, "new content")
        assert output.read_text() == "new content"


class TestGetHash:
    def test_returns_sha256_hex_string(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_text("hello")
        result = get_hash(str(test_file))
        assert len(result) == 64
        assert all(c in "0123456789abcdef" for c in result)

    def test_same_content_same_hash(self, tmp_path):
        file1 = tmp_path / "a.txt"
        file2 = tmp_path / "b.txt"
        file1.write_text("same content")
        file2.write_text("same content")
        assert get_hash(str(file1)) == get_hash(str(file2))

    def test_different_content_different_hash(self, tmp_path):
        file1 = tmp_path / "a.txt"
        file2 = tmp_path / "b.txt"
        file1.write_text("content A")
        file2.write_text("content B")
        assert get_hash(str(file1)) != get_hash(str(file2))


class TestCachedFileLoader:
    def test_loads_yaml_file(self, tmp_path):
        cached_file_loader.cache_clear()
        yaml_file = tmp_path / "test.yaml"
        yaml_file.write_text("key: value\n")
        result = cached_file_loader(yaml_file)
        assert result == {"key": "value"}

    def test_loads_json_file(self, tmp_path):
        cached_file_loader.cache_clear()
        json_file = tmp_path / "test.json"
        json_file.write_text('{"key": "value"}')
        result = cached_file_loader(json_file)
        assert result == {"key": "value"}

    def test_loads_text_file(self, tmp_path):
        cached_file_loader.cache_clear()
        text_file = tmp_path / "test.txt"
        text_file.write_text("plain text content")
        result = cached_file_loader(text_file)
        assert result == "plain text content"

    def test_caches_results(self, tmp_path):
        cached_file_loader.cache_clear()
        yaml_file = tmp_path / "cached.yaml"
        yaml_file.write_text("key: original\n")
        first_result = cached_file_loader(yaml_file)
        yaml_file.write_text("key: modified\n")
        second_result = cached_file_loader(yaml_file)
        assert first_result == second_result
        cached_file_loader.cache_clear()
