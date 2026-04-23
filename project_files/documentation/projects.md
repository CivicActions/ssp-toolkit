# Creating and Loading Projects

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
