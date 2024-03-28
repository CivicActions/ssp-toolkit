"""
Copyright 2019-2024 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#copyright.


Given a YAML file and path to directory of template files, this tool
generates markdown files, replicating the directory structure in the template
directory. It uses the https://github.com/CivicActions/secrender tool for
variable replacement.
"""

from itertools import dropwhile, zip_longest
from pathlib import Path

import click

from tools.helpers import secrender
from tools.helpers.ssptoolkit import find_toc_tag, load_template_args


@click.command()
@click.option(
    "--templates",
    "-t",
    "templates",
    required=False,
    default="templates/",
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
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
def main(templates: str, output_dir: str):
    template_args = load_template_args()
    output_to = Path(output_dir)
    template_dir = Path(templates)
    if not output_to.is_dir():
        output_to.mkdir(parents=True, exist_ok=True)

    template_path = Path(template_dir).rglob("*")
    template_files = [x for x in template_path if x.is_file()]

    for template in template_files:
        new_file = Path(
            rewrite(
                template_file=template,
                template_dir=template_dir,
                output_dir=output_to,
            )
        )
        if new_file.suffix == ".j2":
            new_file = new_file.with_name(new_file.stem)

        if not new_file.parent.is_dir():
            new_file.parent.mkdir(parents=True, exist_ok=True)
        print(f"Creating file: {new_file} from {template}")

        secrender.secrender(
            template_path=template.as_posix(),
            template_args=template_args,
            output_path=new_file.as_posix(),
        )

        find_toc_tag(file=str(new_file))


def rewrite(template_file: Path, template_dir: Path, output_dir: Path) -> str:
    sub_path = [
        p[0]
        for p in dropwhile(
            lambda f: f[0] == f[1], zip_longest(template_file.parts, template_dir.parts)
        )
    ]
    return str(output_dir / Path(*sub_path))


if __name__ == "__main__":
    main()
