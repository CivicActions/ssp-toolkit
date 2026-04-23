# OpenControl

[OpenControl](https://github.com/opencontrol) is an open-source framework for managing compliance documentation. It
provides a structured way to document how a system meets various compliance standards by breaking down controls into
reusable components. The SSP Toolkit uses OpenControl to help organizations create and maintain System Security Plans
(SSPs) efficiently.

## Project Structure

In the root directory of the SSP Toolkit, you will find a file named `opencontrol.yaml`. This file serves as the main
configuration file for the project framework within the SSP Toolkit. It defines the components, standards, and
certifications for the system. The `opencontrol.yaml` file is structured in a way that allows you to specify various
aspects of your compliance documentation, including:

- **Components**: These are the building blocks of your system, representing different parts or services that need to
  be documented for compliance. The file contains a list of paths to the rendered component definition directories.
- **Standards**: These are the compliance frameworks or regulations that your system needs to adhere to, such as NIST
  SP 800-53, ISO 27001, etc.
- **Certifications**: The certifications document list the controls that are applicable to the system based on the selected
  standards.

## Usage

The `opencontrol.yaml` file is structured thusly:

```yaml
schema_version: 1.0.0
name: [SYSTEM NAME]
metadata:
  description: [SYSTEM DESCRIPTION]
  maintainers:
  - [MAINTAINER NAME]
components:
- [PATH TO COMPONENT 1]
- [PATH TO COMPONENT 2]
- ...
standards:
- ./standards/nist-sp-800-53-rev5.yaml
certifications:
- ./certifications/800-53-rev-fisma-low-impact.yaml
```
