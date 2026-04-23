"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

from pathlib import Path

import click
from loguru import logger
from pypandoc import convert_file

from tools.helpers.helpers import get_project_path
from tools.logging_config import setup_logging  # noqa: F401


def render_multiple(
    to_render: Path, file_type: str, output_to: Path, project_path: Path
):
    for file_path in to_render.glob("**/*.md"):
        render_file(
            to_render=file_path,
            file_type=file_type,
            output_to=output_to,
            project_path=project_path,
        )


def render_file(to_render: Path, file_type: str, output_to: Path, project_path: Path):
    args: list = []
    filepath = output_to.joinpath(to_render.stem).with_suffix(f".{file_type}")
    template_file = project_path.joinpath("assets/custom-reference.docx")
    if file_type == "docx" and template_file.exists():
        args.append(f"--reference-doc={template_file.as_posix()}")

    convert_file(
        source_file=to_render,
        to=file_type,
        outputfile=str(filepath),
        extra_args=args,
    )
    logger.info(f"Writing file {filepath.as_posix()}")
    print(f"Writing file {filepath.as_posix()}")


@click.command("export-to")
@click.option(
    "--render",
    "-r",
    "to_render",
    type=click.Path(exists=False, dir_okay=True, file_okay=True, readable=True),
    help="The directory containing the files, or a file, to render.",
)
@click.option(
    "--type",
    "-t",
    "file_type",
    required=False,
    default="docx",
    help="The file type to create using Pandoc (default: docx)",
)
def export_to_cmd(to_render: str, file_type: str):
    """
    Export Markdown files to other formats using Pandoc.

    :param to_render: Path to the Markdown file
    :param file_type: The file type to create using Pandoc (default: docx)
    """

    project_path = get_project_path()

    output_to = project_path / "rendered" / "docx"
    if not output_to.exists():
        output_to.mkdir(exist_ok=False)

    render_path = project_path / to_render
    if render_path.exists():
        if render_path.is_dir():
            render_multiple(
                to_render=render_path,
                file_type=file_type,
                output_to=output_to,
                project_path=project_path,
            )
        else:
            render_file(
                to_render=render_path,
                file_type=file_type,
                output_to=output_to,
                project_path=project_path,
            )
    else:
        logger.error(f"No such file or directory: {render_path.as_posix()}")
        raise FileNotFoundError
