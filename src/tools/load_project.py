"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

from pathlib import Path

import click
from dotenv import set_key
from loguru import logger

from tools.helpers.helpers import load_yaml_files
from tools.logging_config import setup_logging  # noqa: F401


@click.command("load-project")
@click.option(
    "--path",
    "-p",
    "project_path",
    required=True,
    help="The path to an existing project",
)
def load_project_cmd(project_path: str) -> None:
    """
    Load an existing project by setting the PROJECT_PATH in the .env file.

    :param project_path: the path to an existing project
    """
    open_control = Path(project_path) / "opencontrol.yaml"

    if not open_control.exists():
        logger.error(f"Project {project_path} does not exist. Project not loaded.")
        raise click.ClickException("Project path does not exist. Project not loaded.")

    set_key(Path.cwd() / ".env", "PROJECT_PATH", project_path)
    logger.info(f"Project path: {project_path}")
    click.echo(f"Set PROJECT_PATH to {project_path} in .env file")

    project_file = load_yaml_files(file_path=open_control)
    click.echo(f"Project {project_file.get('name', 'DEFAULT')} loaded successfully.")
