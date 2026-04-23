# Keys and Templating

The SSP Toolkit uses the [Jinja2 templating engine](https://jinja.palletsprojects.com/en/stable/) to manage
configuration files and other text-based resources. This allows for dynamic content generation based on predefined
variables and conditions.

## Keys

The `/keys/` directory contains various key files defining key value pairs and lists of values that are used in the
project templates. For instance, the `project.yaml` file may contain key-value pairs that define project-specific values
like project name, the client name, and other values associated with the project. The `regulations.yaml`
key file contains a list of regulations that the project adheres to.

The SSP Toolkit reads these files dynamically, so if a new key file is added to the `/keys/` directory, it will be
automatically included in the templating process without requiring any changes to the codebase. Variable names in the
templates are based on the file names in the `/keys/` directory. For example, variables from `project.yaml` can be
accessed using the `project` prefix (e.g., `{{ project.name }}`).

## Templating

The templates are where you can make changes to the files that will be generated for your project. These templates are
located in the `/templates/` directory and include appendices, front matter files, components and tailoring files. Each
template file uses Jinja2 syntax to reference variables defined in the key files. For example,

```jinja2
The {{ project.name }} does X, Y, and Z for {{ project.client }}.
```

When the SSP Toolkit processes the templates, it replaces the Jinja2 variables with the corresponding values from the
key files.

```text
The AwesomeApp does X, Y, and Z for Acme Agency.
```

Jinj2 also provides control structures like loops and conditionals, allowing for more complex templating logic. For
example, you can use a loop to iterate over a list of regulations defined in the `regulations.yaml` key file:

```jinja2
{% for regulation in regulations.list %}
- {{ regulation }}
{% endfor %}
```
This would generate a list of regulations in the output file based on the contents of the `regulations.yaml` key file.

By leveraging Jinja2 templating and the key files, the SSP Toolkit provides a flexible and dynamic way to generate
project documentation and configuration files tailored to specific project requirements. This also allows us to make
changes in one place (the key files) that automatically propagate throughout all relevant templates.
