# check-config commands

The `check-config` commands lets you read configuration data. There are two commands
that can be used with `getconfig`; `get-value` and `list-files`.

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
`Contractor` key file, you would run `uv run cli getconfig get-value -f contractor -k name_short`.
If you omit the `--key/-k` parameter, for instance `uv run cli getconfig get-value -f contractor`
this will output the entire contents of the key file formatted as YAML.

#### Example

Get a value for a given key in the `contractor.yaml` file:

```shell
uv run cli getconfig get-value -f contractor -k name_short
```

Get the entire contents of the `contractor.yaml` file

```shell
uv run cli getconfig get-value -f contractor
```

#### Usage

```shell
Usage: getconfig get-value [OPTIONS]

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
uv run cli getconfig list-files
```

#### Usage

```shell
Usage: getconfig list-files [OPTIONS]

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
