# Auto-generated System Security Plan (SSP)

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

This repository contains documents and scripts that can be used to create and maintain a System Security Plan (SSP) as required by the [Risk Management Framework (RMF) version 1](https://csrc.nist.gov/publications/detail/sp/800-37/rev-1/archive/2014-06-05). Included are examples of SSP "front matter", control implementation statements (as defined in [NIST SP 800-53r4](https://nvd.nist.gov/800-53/Rev4/) along with the Privacy Overlay), and a collection of appendices.

We understand that version 2 of the [Risk Management Framework for Information Systems and Organizations: A System Life Cycle Approach for Security and Privacy (RMFv2)](https://csrc.nist.gov/publications/detail/sp/800-37/rev-2/final) has been released, and we are planning to update this repository to include the controls as defined in [NIST SP 800-53r5 (draft)](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/draft) as this is finalized.

Control templates are in machine-readable ([OpenControl](https://github.com/opencontrol/)) YAML files. The intention is to enable these files to be updated automatically by gathering evidence on the state of the running system.

### System Security Plan sections

A current version can be viewed in Git Markdown from this repository:

* [Front matter](frontmatter) (points of contact, system and technical description, ...)
* [Control implementation statements](docs/controls.md)
* [Appendices](appendices) (incident response, configuration management, regulations, ...)

## Disclaimer

The contents of these pages are provided as an information guide only. They are
intended to enhance compliance understanding and are not intended to be used
directly as a System Security Plan without agency-specific review

## Prerequisites

You will need [Python Poetry](https://python-poetry.org/docs/) to run the
SSP Toolkit in a Python virtual environment. Once you have Poetry
installed you will be able to run all the commands using the
format `poetry run [COMMAND]`.

To install all the Python dependencies, run `poetry install`.


## Generating the documentation

To update the local Markdown and or to create new exportable files, perform the following steps:

### createfiles

Create/update the frontmatter, components and appendices using [templates](templates) and [keys](keys)

#### Example

```bash
poetry run createfiles -t templates
```

#### Usage

```bash
Usage: createfiles [OPTIONS]

Options:
  -t, --templates DIRECTORY  Template directory
  -o, --out PATH             Output directory (default: current directory)
  --help                     Show this message and exit.
```

### makefamilies

Generate markdown versions of the RMF control implementation family files in the `docs/controls/` directory:

#### Example
```bash
poetry run makefamilies
```

### sop

Generate Standard Operating Procedure (SOP) docs (from `components/` and `keys/sop.yaml`) in the `docs/sop` directory

#### Example
```bash
poetry run sop -c components
```

#### Usage
```bash
Usage: sop [OPTIONS]

Options:
  -c, --components DIRECTORY  Rendered components directory
  -o, --out PATH              Output directory (default: docs/)
  --help                      Show this message and exit.

```

### makessp

Generate System Security Plan (SSP)

#### Example
```bash
poetry run makessp
```

### exportto

Generate Microsoft Word (.docx) versions of the control family, appendices, and frontmatter files (see the `docx/` directory):

#### Example
```bash
poetry run exportto -c docs/controls
```

#### Usage
```bash
Usage: exportto [OPTIONS]

Options:
  -r, --render_file PATH  The directory containing the files, or a file, to
                          render.
  -t, --type TEXT         The file type to create using Pandoc (default: docx)
  -o, --out PATH          Output directory (default: docx)
  --help                  Show this message and exit.
```

### creatematrix

Generate a spreadsheet showing which, if any, components are responsible
for addressing a given control.

#### Example
```bash
poetry run creatematrix
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

Copyright 2019-2024 CivicActions, Inc.
