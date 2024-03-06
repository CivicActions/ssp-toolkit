# Auto-generated System Security Plan (SSP)

<!--ts-->
   * [Auto-generated System Security Plan (SSP)](#auto-generated-system-security-plan-ssp)
      * [Overview](#overview)
         * [System Security Plan sections](#system-security-plan-sections)
         * [Disclaimer](#disclaimer)
      * [Prerequisites](#prerequisites)
         * [Activate your environment](#activate-your-environment)
      * [Generating the documentation](#generating-the-documentation)
      * [OpenControl and OSCAL](#opencontrol-and-oscal)
      * [License](#license)

<!-- Added by: fen, at: Tue 07 Apr 2020 02:53:45 PM EDT -->

<!--te-->

## Overview

This repository contains documents and scripts that can be used to create and maintain a System Security Plan (SSP) as required by the [Risk Management Framework (RMF) version 1](https://csrc.nist.gov/publications/detail/sp/800-37/rev-1/archive/2014-06-05). Included are examples of SSP "front matter", control implementation statements (as defined in [NIST SP 800-53r4](https://nvd.nist.gov/800-53/Rev4/) along with the Privacy Overlay), and a collection of appendices.

We understand that version 2 of the [Risk Management Framework for Information Systems and Organizations: A System Life Cycle Approach for Security and Privacy (RMFv2)](https://csrc.nist.gov/publications/detail/sp/800-37/rev-2/final) has been released and we are planning to update this repository to include the controls as defined in [NIST SP 800-53r5 (draft)](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/draft) as this is finalized.

Control templates are in machine readable ([OpenControl](https://github.com/opencontrol/)) YAML files. The intention is to enable these files to be updated automatically by gathering evidence on the state of the running system.

### System Security Plan sections

A current version can be viewed in Git Markdown from this repository:

* [Front matter](frontmatter) (points of contact, system and technical description, ...)
* [Control implementation statements](docs/controls.md)
* [Appendices](appendices) (incident response, configuration management, regulations, ...)

### Disclaimer

The contents of these pages are provided as an information guide only. They are intended to enhance compliance understanding and are not intended to be used directly as a System Security Plan without agency-specific review.

## Prerequisites

You will need `docker` and `docker-compose` running locally in a `bash` compatible shell. These can be obtained by installing the [Docker Desktop](https://www.docker.com/products/docker-desktop).

```bash
docker --version
docker-compose --version
```

### Activate your environment

We use the [bowline](https://github.com/CivicActions/bowline/) docker sandbox helper to instantiate local containers with [compliancetools](https://github.com/CivicActions/compliancetools) and [secrender](https://github.com/CivicActions/secrender). The following two commands will ***activate*** your local environment, setting up local aliases for the bowline-exposed commands which are described below.

```bash
docker-compose pull
source activate
```

## Generating the documentation

To update the local Markdown and or to create new exportable files, perform the following steps:

1. Create/update the frontmatter, components and appendices using [templates](templates) and [keys](keys)

```bash
createfiles -i configuration.yaml -t templates
```

2. Generate markdown versions of the RMF control implementation family files in the `/docs/controls/` directory:

```bash
mkdir -p docs/controls
makefamilies
```

3. Generate Standard Operating Procedure (SOP) docs (from `components/` and `keys/sop.yaml`) in the `docs/sop` directory

    ```bash
    sop -i configuration.yaml -c components -o docs
    ```

4. Generate Microsoft Word (.docx) versions of the control family files (see the `docx/` directory):

```bash
exportto -c docs/controls
```

5. Generate Microsoft Word (.docx) versions of the appendices and front matter (also in `docx/` directory):

    ```bash
    ./makeDocx.sh
    ```

6. Generate a reponsiblity matrix with:


```bash
creatematrix
```

7. Optional (and temporary) hack to add a Table of Contents (requires <https://github.com/ekalinin/github-markdown-toc> v0.5+ with `gh-md-toc` in your shell search path):

```bash
./makeDocsTOC.sh
```

## OpenControl and OSCAL

The SSP-Toolkit is currently in an extended format of OpenControl in which each component represents its controls in separate [RMF Control Family](https://nvd.nist.gov/800-53/Rev4) files. Use the [compliance-io](https://github.com/CivicActions/compliance-io) tools to convert the SSP-Toolkit to a [compliance-masonry](https://github.com/opencontrol/compliance-masonry)-friendly OpenControl directory and from that generate an [OSCAL component definition](https://pages.nist.gov/OSCAL/documentation/schema/implementation-layer/component/):
```
# You may want to create a python virtual environment for the pip install
pip install git+https://github.com/civicactions/compliance-io.git@main#egg=complianceio
mkdir opencontrol oscal
python library/defenestrate.py opencontrol.yaml opencontrol
python library/oc_to_oscal_components.py opencontrol/opencontrol.yaml > oscal/ssp-toolkit.json
```

See the [compliance-io/README.md](https://github.com/CivicActions/compliance-io/blob/main/README.md) for more information.

## License

GNU General Public License v3.0 or later. Some portions of this work were produced under a Government contract and are licensed under the terms of Creative Commons Zero v1.0 Universal.

SPDX-License-Identifier: `GPL-3.0-or-later`

Copyright 2019-2024 CivicActions, Inc.
