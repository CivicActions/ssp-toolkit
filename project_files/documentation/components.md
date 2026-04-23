# Components

Components are logical grouping of controls by system elements or services. For example, if a system is
on AWS and is using the S3 service, there could be a component called "AWS S3" that includes all the controls
related to the security and compliance of the S3 service. Within that component, there could be different families
of controls, such as "Access Control", "Data Protection", and "Monitoring".

The components use a slightly modified version of the
[OpenControl component schema](https://github.com/opencontrol/schemas/blob/master/kwalify/component/v3.1.0.yaml).
Rather than grouping all controls into a single component file, these components are structured within a
`component.yaml` file which defines the different controls families that the component addresses using the following
format:

```yaml
name: <Component Name>
schema_version: <Component Title>
satisfies:
    - <Control Family Name>
    - <Control Family Name>
    - ...
```

This allows us to separate the controls into smaller, more easily managed files. Each control family is then defined
in its own YAML file within the same directory as the `component.yaml` file. The control family files use the standard
OpenControl control component schema.

```yaml
family: ACCESS CONTROL
documentation_complete: false
satisfies:
- control_key: AC-2
  control_name: ACCOUNT MANAGEMENT
  standard_key: NIST SP 800-53 Revision 5
  covered_by: []
  security_control_type: Shared
  narrative:
  - text: >
      [CONTROL STATEMENT REDACTED FOR BREVITY]
  - key: a
    text: >
      [CONTROL STATEMENT REDACTED FOR BREVITY]
  implementation_status: partial
```

Components that are applicable to the project are then referenced in the `opencontrol.yaml` file, located in the project's
root directory. For more on the `opencontrol.yaml` file, see the [OpenControl project documentation](./opencontrol.md).

In the SSP Toolkit, component templates are located in the `templates/components/` directory. Each component has its own
subdirectory within this directory, containing the `component.yaml` file and the control family files. The templates, like
all the templates in the SSP Toolkit, use [Jinja2 templating syntax](https://jinja.palletsprojects.com/en/stable/) to
allow for dynamic content generation based on values stored in the `keys` directory in the project root. For instance,
we store the project name in a key file called `project.yaml`, which assigns the project name to the variable
`project.name`.

`project.yaml`
```yaml
name: Project Full Name
name_short: Project
```

This variable can then be used in the component:

```yaml
The {{ project.name }} uses AWS S3 to store user data securely within the {{ project.name_short }} application.
```

For more information on keys and templating, see the [Keys and Templating documentation](./keys_and_templating.md).
