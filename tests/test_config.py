"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import pytest

from tools.config import Config


class TestConfig:
    def test_loads_config(self, project_env):
        config = Config()
        assert config.config is not None

    def test_raises_when_configuration_missing(self, tmp_path, monkeypatch):
        (tmp_path / "opencontrol.yaml").write_text(
            "schema_version: '1.0.0'\nname: T\nmetadata:\n  description: T\n"
        )
        monkeypatch.setenv("PROJECT_PATH", str(tmp_path))
        with pytest.raises(FileNotFoundError, match="configuration.yaml"):
            Config()

    def test_check_config_values_returns_section(self, project_env):
        config = Config()
        result = config.check_config_values(file="system_security_plan")
        assert isinstance(result, dict)
        assert "title" in result

    def test_check_config_values_returns_key_value(self, project_env):
        config = Config()
        result = config.check_config_values(file="system_security_plan", key="title")
        assert "Test System Security Plan" in result

    def test_check_config_values_missing_file_returns_empty(self, project_env):
        config = Config()
        result = config.check_config_values(file="nonexistent_section")
        assert result == {}

    def test_check_config_values_missing_key_returns_empty(self, project_env):
        config = Config()
        result = config.check_config_values(
            file="system_security_plan", key="nonexistent_key"
        )
        assert result == ""

    def test_loads_key_files(self, project_env):
        # Add a key file to verify load_keys picks it up
        keys_dir = project_env / "keys"
        key_file = keys_dir / "custom-key.yaml"
        key_file.write_text("setting: enabled\n")
        config = Config()
        assert "custom-key" in config.config

    def test_default_key_aliases(self, project_env):
        keys_dir = project_env / "keys"
        (keys_dir / "artifacts.yaml").write_text("artifact_list:\n  - item1\n")
        config = Config()
        assert "artifact" in config.config

    def test_config_files_list_populated(self, project_env):
        keys_dir = project_env / "keys"
        (keys_dir / "some-file.yaml").write_text("key: value\n")
        config = Config()
        filenames = [f[0] for f in config.config_files]
        assert "some-file.yaml" in filenames
