# Example tool to render a template using data loaded from a YAML
# file.  One intended use case: load an OSCAL style YAML file and render
# a Jinja2 template to produce the markdown for SSP front matter.
#
# To better support the above intended use case, by default
# the value of the key 'system_security_plan' in the input values YAML
# is mapped to the template variable 'ssp'.
#
# # secrender --in ssp.yaml --template ssp.md.j2 >ssp.md

# TODO
# - would be nice to validate input values against schema
# - root element handling is simplistic

import datetime
import os

import click
import jinja2
from yaml import FullLoader, load
from yamlinclude import YamlIncludeConstructor


@click.command()
@click.option(
    "--in",
    "-i",
    "in_",
    required=True,
    type=click.Path(exists=True, dir_okay=False, readable=True),
    help="values (YAML)",
)
@click.option(
    "--template",
    "-t",
    "template_path",
    type=click.Path(exists=True, dir_okay=False, readable=True),
    required=True,
    help="Template (Jinja2)",
)
@click.option(
    "--root",
    "-R",
    help="If supplied, names a Jinja2 variable that will hold all the top-level "
    "YAML values.",
)
@click.option(
    "--set",
    "-s",
    "set_",
    nargs=2,
    multiple=True,
    help="Set a value.  E.g., -s var value",
)
@click.option(
    "--output",
    "-o",
    "output_file",
    type=click.Path(exists=False, allow_dash=True),
    default="-",
    help="Output file (or - for stdout)",
)
@click.option(
    "--output-dir",
    "-O",
    "output_dir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    help="Default output directory",
)
def main(
    in_: str,
    template_path: str,
    root: str,
    set_: dict,
    output_file: str,
    output_dir: str,
):
    YamlIncludeConstructor.add_to_loader_class(loader_class=FullLoader)

    with open(in_, "r") as stream:
        yaml = load(stream, Loader=FullLoader)

    template_args = get_template_args(yaml, root, set_)
    output_path = make_output_path(output_file, output_dir)

    secrender(template_path, template_args, output_path)


def secrender(template_path: str, template_args: dict, output_path: str):
    template = get_template(template_path)
    rendered = template.render(**template_args)

    with open(output_path, "w") as output:
        print(rendered, file=output)


def get_template(template_path: str) -> jinja2.Template:
    abs_path = os.path.abspath(template_path)
    template_dir, template_file = os.path.split(abs_path)
    template_loader = jinja2.FileSystemLoader(searchpath=template_dir)
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(template_file)

    return template


def make_output_path(output_file: str, output_dir: str) -> str:
    if output_file == "-":
        return "/dev/stdout"
    elif os.path.isabs(output_file) or output_dir is None:
        return output_file
    else:
        return os.path.join(output_dir, output_file)


def get_template_args(yaml: dict, root: str, set_: dict) -> dict:
    """
    Return a dictionary of arguments to pass to the template from the YAML file.

    :param yaml: A dictionary of YAML attributes.
    :param root: A string representing the root YAML object.
    :param set_: A dictionary
    :return:
    """
    template_args: dict = {}

    if root:
        target: dict = {}
        template_args[root] = target
    else:
        target = template_args

    for key, value in yaml.items():
        target[key] = value

    if set_:
        for (key, value) in set_.items():
            template_args[key] = value

    template_args["current_date"] = datetime.datetime.today()

    return template_args


if __name__ == "__main__":
    main()
