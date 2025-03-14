"""
Copyright 2019-2024 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

from pathlib import Path

import click
from pypandoc import convert_file


def render_multiple(to_render: Path, file_type: str, output_to: Path):
    for file_path in to_render.glob("**/*.md"):
        render_file(to_render=file_path, file_type=file_type, output_to=output_to)


def render_file(to_render: Path, file_type: str, output_to: Path):
    args: list = []
    filepath = output_to.joinpath(to_render.stem).with_suffix(f".{file_type}")
    if file_type == "docx" and Path("assets/custom-reference.docx").exists():
        args.append("--reference-doc=assets/custom-reference.docx")

    convert_file(
        source_file=to_render,
        to=file_type,
        outputfile=str(filepath),
        extra_args=args,
    )
    print(f"Writing file {filepath.as_posix()}")


@click.command()
@click.option(
    "--render_file",
    "-r",
    "render",
    type=click.Path(exists=True, dir_okay=True, file_okay=True, readable=True),
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
@click.option(
    "--out",
    "-o",
    "output",
    type=click.Path(exists=False, dir_okay=True, readable=True),
    default="docx",
    help="Output directory (default: docx)",
)
def main(render: str, file_type: str, output: str):
    output_to = Path(output)
    if not output_to.exists():
        output_to.mkdir(exist_ok=False)

    to_render = Path(render)
    if to_render.exists():
        if to_render.is_dir():
            render_multiple(
                to_render=to_render, file_type=file_type, output_to=output_to
            )
        else:
            render_file(to_render=to_render, file_type=file_type, output_to=output_to)
    else:
        raise FileNotFoundError


if __name__ == "__main__":
    main()
