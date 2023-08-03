# Copyright 2019-2020 CivicActions, Inc. See the README file at the top-level
# directory of this distribution and at https://github.com/CivicActions/compliancetools#copyright.
#
# Given a YAML file and path to directory of template files, this tool
# generates markdown files, replicating the directory structure in the template
# directory. It uses the https://github.com/CivicActions/secrender tool for
# variable replacement.

import mmap
from itertools import dropwhile, zip_longest
from pathlib import Path

import click
import md_toc
from yaml import FullLoader, load  # type: ignore
from yamlinclude import YamlIncludeConstructor

import tools.lib.secrender as secrender


@click.command()
@click.option(
    "--in",
    "-i",
    "in_",
    required=True,
    type=click.Path(exists=True, dir_okay=False, readable=True),
    help="Replacement data values (YAML)",
)
@click.option(
    "--templates",
    "-t",
    "template_dir",
    required=True,
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
    help="Template directory",
)
@click.option(
    "--out",
    "-o",
    "out_",
    type=click.Path(exists=False, dir_okay=True, readable=True),
    default=".",
    help="Output directory (default: current directory)",
)
def main(in_: str, template_dir: str, out_: str):
    template_args = load_template_args(in_)
    od = Path(out_)
    td = Path(template_dir)
    if not od.is_dir():
        od.mkdir(parents=True, exist_ok=True)

    p = Path(td).rglob("*")
    templates = [x for x in p if x.is_file()]

    for tf in templates:
        new_path = rewrite(tf, td, od)
        new_file = Path(new_path)
        ext = new_file.suffix
        if ext == ".j2":
            new_file = new_file.with_name(new_file.stem)

        if not new_file.parent.is_dir():
            new_file.parent.mkdir(parents=True, exist_ok=True)
        print("Creating file: {} from {}".format(new_file, tf))
        secrender.secrender(tf, template_args, new_file)

        find_toc_tag(str(new_file))


def load_template_args(in_):
    YamlIncludeConstructor.add_to_loader_class(loader_class=FullLoader)
    with open(in_, "r", newline="") as stream:
        yaml = load(stream, Loader=FullLoader)
    return secrender.get_template_args(yaml, None, dict())


def rewrite(tf, td, od):
    subpath = [
        p[0] for p in dropwhile(lambda f: f[0] == f[1], zip_longest(tf.parts, td.parts))
    ]
    return str(od / Path(*subpath))


def find_toc_tag(file):
    with open(file, "rb", 0) as f, mmap.mmap(
        f.fileno(), 0, access=mmap.ACCESS_READ
    ) as s:
        if s.find(b"<!--TOC-->") != -1:
            write_toc(file)


def write_toc(file):
    toc = md_toc.build_toc(file, keep_header_levels=3, skip_lines=5)
    md_toc.write_string_on_file_between_markers(file, toc, "<!--TOC-->")


if __name__ == "__main__":
    main()
