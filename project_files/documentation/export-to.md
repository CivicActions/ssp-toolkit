# export-to Command

The `export-to` command allows you to export project Markdown files to `.docx` files using
[Pandoc](https://pandoc.org/). This is useful for generating Word documents of your project's
System Security Plan (SSP), appendices, or other documentation.

## Usage

To export a Markdown file to a `.docx` file, use the following command:

```shell
uv run cli export-to --render [PATH TO MARKDOWN FILE OR DIRECTORY]
```

This command will generate a `.docx` file to the `/rendered/docx/` directory within your
project folder. It is possible to export other file types supported by Pandoc by using the
`--type` option. For example, to export to PDF:

```shell
uv run cli export-to --render [PATH TO MARKDOWN FILE OR DIRECTORY] --type pdf
```

```shell
Usage: cli export-to [OPTIONS]

  Export Markdown files to other formats using Pandoc.

  :param to_render: Path to the Markdown file :param file_type: The file type
  to create using Pandoc (default: docx)

Options:
  -r, --render PATH  The directory containing the files, or a file, to render.
  -t, --type TEXT    The file type to create using Pandoc (default: docx)
  --help             Show this message and exit.
```

## Customizing the Pandoc template

Pandoc uses a template, `custom-reference.dox`, located in the `/assets` folder of your project
directory. This file can be customized to match agency or organization requirements.  For more
information see the [Pandoc documentation](https://pandoc.org/MANUAL.html#option--reference-doc).
