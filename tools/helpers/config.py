from pathlib import Path

import click
import yaml


class Config:
    config: dict
    configuration: Path = Path("configuration.yaml")
    keys: Path = Path("keys")
    default_keys: dict = {
        "responsibility.yaml": "status",
        "info_system.yaml": "information_system",
        "config-management.yaml": "cm",
        "justifications.yaml": "justify",
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
            print(f"Loading {filename.name}")
            key = self.default_keys.get(filename.name, filename.stem)
            with open(filename, "r") as fp:
                self.config[key] = yaml.load(fp, Loader=yaml.FullLoader)

    def check_config(self, key: str = "", verbose: bool = False):
        if key:
            print(yaml.dump(self.config.get(key, {})))
        else:
            print(yaml.dump(self.config, default_flow_style=False, indent=4, width=80))


@click.command()
@click.option(
    "--key",
    "-k",
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
)
def main(key: str = "", verbose: bool = False):
    config = Config()
    if key and not verbose:
        print(config.check_config())


if __name__ == "__main__":
    main()
