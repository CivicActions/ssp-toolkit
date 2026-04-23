"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-flask#license.

Example tool to render a template using data loaded from a YAML
file.  One intended use case: load an OSCAL style YAML file and render
a Jinja2 template to produce the markdown for SSP front matter.

To better support the above intended use case, by default
the value of the key 'system_security_plan' in the input values YAML
is mapped to the template variable 'ssp'.

# secrender --in ssp.yaml --template ssp.md.j2 >ssp.md

TODO
- would be nice to validate input values against schema
- root element handling is simplistic
"""

import datetime
import os

import jinja2


def secrender(template_path: str, template_args: dict, output_path: str):
    template = get_template(template_path)
    rendered = template.render(**template_args)

    with open(output_path, "w") as output:
        print(rendered, file=output)


def get_template(template_path: str) -> jinja2.Template:
    abs_path = os.path.abspath(template_path)
    template_dir, template_file = os.path.split(abs_path)
    template_loader = jinja2.FileSystemLoader(searchpath=template_dir)
    template_env = jinja2.Environment(loader=template_loader, autoescape=True)
    template = template_env.get_template(template_file)

    return template


def make_output_path(output_file: str, output_dir: str) -> str:
    if output_file == "-":
        return "/dev/stdout"
    elif os.path.isabs(output_file) or output_dir is None:
        return output_file
    else:
        return os.path.join(output_dir, output_file)


def get_template_args(yaml: dict, set_: dict, root: str = "") -> dict:
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
        for key, value in set_.items():
            template_args[key] = value

    template_args["current_date"] = datetime.datetime.today()

    return template_args
