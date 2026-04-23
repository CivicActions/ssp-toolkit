# Auto-generated System Security Plan (SSP)

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

<!--ts-->
   * [Auto-generated System Security Plan (SSP)](#auto-generated-system-security-plan-ssp)
      * [Overview](#overview)
         * [System Security Plan sections](#system-security-plan-sections)
         * [Disclaimer](#disclaimer)
      * [Prerequisites](#prerequisites)
      * [Generating the documentation](#generating-the-documentation)
      * [OpenControl and OSCAL](#opencontrol-and-oscal)
      * [License](#license)

<!-- Added by: fen, at: Tue 07 Apr 2020 02:53:45 PM EDT -->

<!--te-->

## Overview

This repository contains documents and scripts that can be used to create and maintain a System Security Plan (SSP) as
required by the [Risk Management Framework (RMF) version 1](https://csrc.nist.gov/publications/detail/sp/800-37/rev-1/archive/2014-06-05). Included are examples of SSP "front matter", control implementation statements (as defined in [NIST SP 800-53r4](https://nvd.nist.gov/800-53/Rev4/) along with the Privacy Overlay), and a collection of appendices.

Control templates are in machine-readable ([OpenControl](https://github.com/opencontrol/)) YAML files. The intention is to enable these files to be updated automatically by gathering evidence on the state of the running system.


## Disclaimer

The contents of these pages are provided as an information guide only. They are
intended to enhance compliance understanding and are not intended to be used
directly as a System Security Plan without agency-specific review

## Prerequisites

You will need the [uv](https://docs.astral.sh/uv/) package manager to run the SSP Toolkit in uv virtual environment.
Once you have uv installed you will be able to run all the commands using the format
`uv run cli [COMMAND]`.

To install all the Python dependencies, run `uv sync`.

## Generating the documentation

To update the local Markdown and or to create new exportable files, perform the following steps:

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

## Creating a new project

To create a new project directory with the SSP-Toolkit structure, run the following command:

```shell
uv run cli create-project -n [PROJECT_NAME] -d [DIRECTORY]
```

This will create a new project within the directory indicated by the `-d` parameter. The project
cannot live within the SSP-Toolkit directory itself. The new project directory will contain all
the templates and files required to generate the SSP documentation. Once a project is created,
you can update the `keys/` directory with your project-specific information and update the templates
and components as required.

Projects should be kept in their own version control repository to track changes over time. Only files
specific to the project should be kept in version control; the SSP-Toolkit itself should not be copied
into the project repository.

### Usage

```shell
Usage: cli create-project [OPTIONS]

  Create a new project directory with the given name.

Options:
  -n, --name TEXT       Name of the new project  [required]
  -d, --directory TEXT  Directory to create the new project in (default:
                        current directory)  [required]
  --help                Show this message and exit.
```

## Loading a project

To load an existing project, run the following command:

```shell
uv run cli load-project -p [PROJECT_PATH]
```

Loading a project will set the `PROJECT_PATH` variable in the `.env` file to the path specified
by the `-p` parameter. This will allow all subsequent commands to run within the context of
the specified project.

### Usage

```shell
Usage: cli load-project [OPTIONS]

  Load an existing project by setting the PROJECT_PATH in the .env file.

  :param project_path: the path to an existing project

Options:
  -p, --path TEXT  The path to an existing project  [required]
  --help           Show this message and exit.
```

### create-files command

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

### make-families command

Generate Markdown versions of the RMF control implementation family files in the `docs/controls/` directory:

#### Example

```shell
uv run cli make-families
```

#### Usage

```shell
Usage: cli make-families [OPTIONS]

  Create control family files from project data.

Options:
  --help  Show this message and exit.
```

### sop command

Generate Standard Operating Procedure (SOP) docs (from `components/` and `keys/sop.yaml`) in the `docs/sop` directory

#### Example

```shell
uv run cli sop
```

#### Usage

```shell
Usage: cli sop [OPTIONS]

  Generate Standard Operating Procedure (SOP) Markdown files from rendered

Options:
  --help  Show this message and exit.
```

### make-ssp command

Generate System Security Plan (SSP)

#### Example

```shell
uv run cli make-ssp
```

#### Usage

```shell
Usage: cli make-ssp [OPTIONS]

  Generate a System Security Plan (SSP) from the control families.

Options:
  --help  Show this message and exit.
```

### export-to command

Generate Microsoft Word (.docx) versions of the control family, appendices, and frontmatter files
(see the `docx/` directory):

`exportto` uses the Pandoc file generation library. Go to the
[install Pandoc page](https://pandoc.org/installing.html) to learn how to install Pandoc locally.

On macOS you can use Homebrew:

```shell
brew install pandoc
```

#### Example

```shell
uv run cli export-to -c docs/controls
```

#### Usage

```shell
Usage: export-to [OPTIONS]

  Export Markdown files to other formats using Pandoc.

  :param to_render: Path to the Markdown file :param file_type: The file type
  to create using Pandoc (default: docx)

Options:
  -r, --render PATH  The directory containing the files, or a file, to
                          render.
  -t, --type TEXT         The file type to create using Pandoc (default: docx)
  -o, --out PATH          Output directory (default: docx)
  --help                  Show this message and exit.
```

### create-matrix command

Generate a spreadsheet showing which, if any, components are responsible
for addressing a given control.

#### Example

```shell
uv run cli create-matrix
```

#### Usage

```shell
Usage: cli create-matrix [OPTIONS]

  Create a responsibility matrix for the SSP components.

Options:
  --help  Show this message and exit.
```

## check-config commands

The `get-config` command lets you read configuration data. There are two commands
that can be used with `get-config`; `get-value` and `list-files`.

### Usage

```shell
Usage: check-config [OPTIONS] COMMAND [ARGS]...

  Check configuration files and keys in the project

Options:
  --help  Show this message and exit.

Commands:
  get-value   Get the value of a specific configuration key from a file
  list-files  List all the files loaded from the keys directory
```

### get-value command

`get-value` is used to get the value of a given key in the configuration dictionary.
For instance if you wanted to know the value of the `name_short` parameter in the
`Contractor` key file, you would run `uv run cli get-config get-value -f contractor -k name_short`.
If you omit the `--key/-k` parameter, for instance `uv run cli get-config get-value -f contractor`
this will output the entire contents of the key file formatted as YAML.

#### Example

Get a value for a given key in the `contractor.yaml` file:

```shell
uv run cli get-config get-value -f contractor -k name_short
```

Get the entire contents of the `contractor.yaml` file

```shell
uv run cli get-config get-value -f contractor
```

#### Usage

```shell
Usage: check-config get-value [OPTIONS]

  Get the value of a specific configuration key from a file

Options:
  -f, --file TEXT  [required]
  -k, --key TEXT   The name of the configuration key whose value should be
                   shown.
  --help           Show this message and exit.
```

### list-files command

The `list-files` command will list all the files loaded from the keys directory.
Most files are keyed using in the filename, for instance the values in the `contractor.yaml`
file would be accessible using the Jinja2 variable `{{ contractor.some_variable }}`, but a few
files have aliases which are used for their key, for instance `configuration-management.yaml`
is aliased to `cm`, so would be available as `{{ cm.some_variable }}`. `list-files` will show a
list of the files and their alias.

#### Example

```shell
uv run cli get-config list-files
```

#### Usage

```shell
Usage: check-config list-files [OPTIONS]

  List all the files loaded from the keys directory

Options:
  --help  Show this message and exit.
```

#### Example results

```shell
Key files and configuration keys:
---------------------------------
contractor.yaml using alias contractor
regulations.yaml using alias regulations
justifications.yaml using alias justify
```

## OpenControl and OSCAL

The SSP-Toolkit is currently in an extended format of OpenControl in which each component represents its controls in separate [RMF Control Family](https://nvd.nist.gov/800-53/Rev4) files. Use the [compliance-io](https://github.com/CivicActions/compliance-io) tools to convert the SSP-Toolkit to a [compliance-masonry](https://github.com/opencontrol/compliance-masonry)-friendly OpenControl directory and from that generate an [OSCAL component definition](https://pages.nist.gov/OSCAL/documentation/schema/implementation-layer/component/):


See the [compliance-io/README.md](https://github.com/CivicActions/compliance-io/blob/main/README.md) for more information.

```
# You may want to create a python virtual environment for the pip install
pip install git+https://github.com/civicactions/compliance-io.git@main#egg=complianceio
mkdir opencontrol oscal
python library/defenestrate.py opencontrol.yaml opencontrol
python library/oc_to_oscal_components.py opencontrol/opencontrol.yaml > oscal/ssp-toolkit.json
```


## License

GNU General Public License v3.0 or later. Some portions of this work were produced under a Government contract and are licensed under the terms of Creative Commons Zero v1.0 Universal.

SPDX-License-Identifier: `GPL-3.0-or-later`

Copyright 2019-2026 CivicActions, Inc.
