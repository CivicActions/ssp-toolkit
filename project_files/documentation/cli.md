## cli commands

The SSP-Toolkit uses [Click](https://click.palletsprojects.com/) to provide a command line interface (CLI) for generating and managing the SSP documentation. The CLI commands are run using the `uv run cli [COMMAND]` format.
The available commands are:

```shell
Usage: cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create-files    Render files from templates using secrender.
  create-matrix   Create a responsibility matrix for the SSP components.
  create-project  Create a new project directory with the given name.
  export-to       Export Markdown files to other formats using Pandoc.
  load-project    Load an existing project by setting the PROJECT_PATH in...
  make-families   Create control family files from project data.
  make-ssp        Generate a System Security Plan (SSP) from the control...
  sop             Generate Standard Operating Procedure (SOP) Markdown...
```
