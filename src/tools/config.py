"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import click
import yaml
from loguru import logger

from tools.helpers.helpers import get_project_path, load_yaml_files
from tools.logging_config import setup_logging  # noqa: F401


class Config:
    config: dict
    keys: dict
    config_files: list[tuple[str, str]] = []
    default_keys: dict = {
        "artifacts.yaml": "artifact",
        "config-management.yaml": "cm",
        "info_system.yaml": "information_system",
        "justifications.yaml": "justify",
    }

    def __init__(self):
        self.project_path = get_project_path()
        if self.project_path.joinpath("configuration.yaml").exists():
            self.config = load_yaml_files(
                self.project_path.joinpath("configuration.yaml")
            )
        else:
            logger.error("configuration.yaml not found in project root.")
            raise FileNotFoundError("configuration.yaml not found in project root.")
        self.load_keys()

    def load_keys(self):
        for filename in self.project_path.joinpath("keys").glob("*.yaml"):
            key = self.default_keys.get(filename.name, filename.stem)
            self.config_files.append((filename.name, key))
            self.config[key] = load_yaml_files(file_path=filename)

    def check_config_values(self, file: str, key: str = "") -> str | dict:
        file_values = self.config.get(file, {})
        values: str | dict = file_values
        if key and file_values:
            values = file_values.get(key, "")
        return values


@click.group("get-config")
def check_config():
    """Check configuration files and keys in the project"""
    pass


@check_config.command("get-value")
@click.option(
    "--file",
    "-f",
    required=True,
)
@click.option(
    "--key",
    "-k",
    required=False,
    help="The name of the configuration key whose value should be shown.",
)
def get_value(file: str, key: str = ""):
    """Get the value of a specific configuration key from a file"""
    config = Config()
    click.echo(yaml.dump(config.check_config_values(file=file, key=key), indent=4, width=80))


@check_config.command("list-files")
def list_files():
    """List all the files loaded from the keys directory"""
    config = Config()
    click.echo("Key files and configuration keys:")
    click.echo("---------------------------------")
    for files in config.config_files:
        click.echo(f"{files[0]} using alias {files[1]}")
