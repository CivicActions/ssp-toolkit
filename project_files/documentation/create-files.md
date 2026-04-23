# create-files command

Create/update the frontmatter, components and appendices using `templates` and `keys` found in the
project directory:

#### Example

```shell
uv run cli create-files -t templates
```

This command will read the templates from the `templates/` directory in the project path and the key files from the
`keys/` directory in the project path, and create files in the projects `rendered/` directory. Inside the `rendered/`
directory the files will maintain the same structure as the `templates/` directory.

#### Usage

```shell
Usage: create-files [OPTIONS]

  Render files from templates using secrender.

  :param templates: Path to the template directory

Options:
  -t, --templates DIRECTORY  Template directory
  --help                     Show this message and exit.
```
