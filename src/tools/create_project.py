"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import shutil
from pathlib import Path

import click
from dotenv import set_key
from loguru import logger

from tools.helpers.helpers import load_yaml_files, write_yaml_files
from tools.logging_config import setup_logging  # noqa: F401


def copy_project_files(new_project_directory: Path) -> None:
    """
    Copy all directories from the project_files directory into the project directory.

    :param new_project_directory: the project directory path
    """
    project_files_dir = Path(__file__).parent.parent.parent / "project_files"
    if not project_files_dir.exists() or not project_files_dir.is_dir():
        click.echo(
            f"project_files directory not found at {project_files_dir.resolve()}"
        )
        logger.error(
            f"project_files directory not found at {project_files_dir.resolve()}"
        )
        return

    try:
        shutil.copytree(project_files_dir, new_project_directory, dirs_exist_ok=False)
        click.echo(f"New Project created in {new_project_directory.as_posix()}")
        logger.info(f"New Project created in {new_project_directory.as_posix()}")
    except FileExistsError as fee:
        click.echo(f"""
PROJECT CREATION ERROR
----------------------
Project {new_project_directory.name} already exists.
Try opening the project using `uv run open-project --directory {new_project_directory.as_posix()}` or
create a new project with a different name.
""")
        logger.error(f"Project {new_project_directory.name} already exists: {fee}")
    except shutil.Error as err:
        click.echo(
            f"Error creating project in {new_project_directory.as_posix()}: {err}"
        )
        logger.error(
            f"Error creating project in {new_project_directory.as_posix()}: {err}"
        )


def update_project_files(project_name: str, project_directory: Path) -> None:
    """
    Create a prepopulated opencontrol.yaml file in the project directory.

    :param project_name: the name of the project
    :param project_directory: the directory path
    """
    opencontrol_path = project_directory / "opencontrol.yaml"
    oc_file = load_yaml_files(file_path=opencontrol_path)
    oc_file["name"] = project_name
    write_yaml_files(file_path=opencontrol_path, content=oc_file)

    click.echo(f"Updated opencontrol.yaml in {opencontrol_path.resolve()}")
    logger.info(f"Updated opencontrol.yaml in {opencontrol_path.resolve()}")

    configuration_path = project_directory / "configuration.yaml"
    config = load_yaml_files(file_path=configuration_path)
    config["system_security_plan"]["title"] = project_name
    write_yaml_files(file_path=configuration_path, content=config)

    click.echo(f"Updated configuration.yaml in {configuration_path.resolve()}")
    logger.info(f"Updated configuration.yaml in {configuration_path.resolve()}")


def check_new_project_location(new_project_directory: Path) -> None:
    """
    Check if the new project directory already exists.

    :param new_project_directory: the directory path
    :return: True if the directory does not exist, False otherwise
    """

    current_project_root = Path(__file__).parent.parent.parent.resolve()
    new_project_dir_resolved = new_project_directory.resolve()
    if str(new_project_dir_resolved).startswith(str(current_project_root)):
        logger.error(
            f"Attempted to create project inside Toolkit directory: {new_project_dir_resolved}"
        )
        raise ValueError(
            f"New project directory cannot be inside the Toolkit directory: {new_project_dir_resolved}."
        )


@click.command("create-project")
@click.option(
    "--name",
    "-n",
    "project_name",
    required=True,
    help="Name of the new project",
)
@click.option(
    "--directory",
    "-d",
    "projects_directory",
    required=True,
    default=".",
    help="Directory to create the new project in (default: current directory)",
)
def create_project_cmd(project_name: str, projects_directory: str) -> None:
    """
    Create a new project directory with the given name.

    :param project_name: Name of the new project
    :param projects_directory: Directory to create the new project in
    """

    project_path = Path(projects_directory) / project_name.replace(" ", "_").lower()
    check_new_project_location(new_project_directory=project_path)
    copy_project_files(new_project_directory=project_path)
    update_project_files(project_name=project_name, project_directory=project_path)

    set_key(Path.cwd() / ".env", "PROJECT_PATH", str(project_path.resolve()))
