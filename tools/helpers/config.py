from pathlib import Path

import click
import yaml


class Config:
    config: dict
    configuration: Path = Path("configuration.yaml")
    keys: Path = Path("keys")
    config_files: list[()] = []
    default_keys: dict = {
        "artifacts.yaml": "artifact",
        "config-management.yaml": "cm",
        "info_system.yaml": "information_system",
        "justifications.yaml": "justify",
        "responsibility.yaml": "status",
    }

    def __init__(self):
        if self.configuration.exists():
            try:
                with open(self.configuration, "r") as fp:
                    self.config = yaml.load(fp, Loader=yaml.FullLoader)
            except IOError:
                print(f"Error loading {self.configuration.as_posix}.")
        else:
            raise FileNotFoundError("configuration.yaml not found in project root.")
        self.load_keys()

    def load_keys(self):
        for filename in self.keys.glob("*.yaml"):
            key = self.default_keys.get(filename.name, filename.stem)
            self.config_files.append((filename.name, key))
            with open(filename, "r") as fp:
                self.config[key] = yaml.load(fp, Loader=yaml.FullLoader)

    def check_config_values(self, file: str, key: str = "") -> str | dict:
        if key:
            values = self.config.get(file, {}).get(key, "")
        else:
            values = self.config.get(file, {})
        return values


@click.group()
@click.pass_context
def check_config(ctx):
    ctx.obj = Config()


@check_config.command()
@click.option(
    "--file",
    "-f",
    required=True,
)
@click.option(
    "--key",
    "-k",
    required=False,
    help="The name of the configuration key whose value should be shown.",
)
@click.pass_context
def get_value(ctx, file: str, key: str = ""):
    config = ctx.obj
    if key:
        click.echo(config.check_config_values(file, key))
    else:
        click.echo(yaml.dump(config.check_config_values(file), indent=4, width=80))


@check_config.command()
@click.pass_context
def list_files(ctx):
    config = ctx.obj
    click.echo("Key files and configuration keys:")
    click.echo("---------------------------------")
    for files in config.config_files:
        click.echo(f"{files[0]} using alias {files[1]}")


if __name__ == "__main__":
    check_config()
