"""
Copyright 2019-2025 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#copyright.


Given a YAML file and path to directory of template files, this tool
generates markdown files, replicating the directory structure in the template
directory. It uses the https://github.com/CivicActions/secrender tool for
variable replacement.
"""

from pathlib import Path

import click

from tools.helpers import secrender
from tools.helpers.ssptoolkit import find_toc_tag, load_template_args


@click.command()
@click.option(
    "--templates",
    "-t",
    "input_template",
    required=False,
    default="templates/",
    type=click.Path(exists=True, dir_okay=True, file_okay=True),
    help="Template directory",
)
@click.option(
    "--out",
    "-o",
    "output_dir",
    type=click.Path(exists=False, dir_okay=True, readable=True),
    default=".",
    required=False,
    help="Output directory (default: current directory)",
)
def main(input_template: str, output_dir: str):
    template_args = load_template_args()
    output_to = Path(output_dir)
    templates = Path(input_template)
    if not output_to.is_dir():
        output_to.mkdir(parents=True, exist_ok=True)

    if templates.is_dir():
        template_path = Path(templates).rglob("*")
        template_files = [
            template_file for template_file in template_path if template_file.is_file()
        ]
    elif templates.is_file():
        template_files = [templates]
    else:
        raise FileNotFoundError(f"{templates.as_posix()} doesn't exist")

    for template in template_files:
        new_file = Path("results").joinpath(*template.parts[1:])
        new_file = (
            new_file.with_name(new_file.stem) if new_file.suffix == ".j2" else new_file
        )

        if not new_file.parent.is_dir():
            new_file.parent.mkdir(parents=True, exist_ok=True)
        print(f"Creating file: {new_file} from {input_template}")

        secrender.secrender(
            template_path=input_template,
            template_args=template_args,
            output_path=new_file.as_posix(),
        )

        find_toc_tag(file=str(new_file))


if __name__ == "__main__":
    main()
