"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import hashlib
import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger
from ruamel.yaml import YAML, YAMLError

from tools.logging_config import setup_logging  # noqa: F401

load_dotenv()


def get_project_path() -> Path:
    project_path_str = os.getenv("PROJECT_PATH")
    if not project_path_str:
        logger.error("PROJECT_PATH environment variable is not set.")
        raise ValueError("PROJECT_PATH environment variable is not set.")

    project_path = Path(project_path_str)
    if not project_path.joinpath("opencontrol.yaml").exists():
        logger.error(f"No opencontrol.yaml found in {project_path.as_posix()}.")
        raise FileNotFoundError(
            f"No opencontrol.yaml found in {project_path.as_posix()}."
        )

    return project_path


@lru_cache(maxsize=128)
def cached_file_loader(filepath: Path | str) -> dict | str:
    file_path = Path(filepath) if isinstance(filepath, str) else filepath
    if file_path.suffix == ".yaml" or file_path.suffix == ".yml":
        return load_yaml_files(file_path)
    elif file_path.suffix == ".json":
        import json

        with open(file_path, "r") as f:
            return json.load(f)
    else:
        with open(file_path, "r") as f:
            return f.read()


def load_yaml_files(file_path: str | Path) -> dict:
    load_file = Path(file_path) if isinstance(file_path, str) else file_path
    try:
        with open(load_file, "r") as fp:
            yaml = YAML(typ="safe", pure=True)
            try:
                project = yaml.load(fp)
                return project
            except YAMLError as e:
                logger.error(f"YAML error in {load_file.name}: {e}")
                return {}
    except FileNotFoundError:
        logger.error(f"No {load_file.name} found in {load_file.parent.as_posix()}.")
        return {}


def write_yaml_files(file_path: str | Path, content: dict) -> None:
    write_yaml = Path(file_path) if isinstance(file_path, str) else file_path
    if not write_yaml.suffix == ".yaml":
        logger.error(f"Incorrect file extension {write_yaml.name}: {write_yaml.suffix}")
        raise YAMLError(f"Incorrect file extension {write_yaml.name}")

    if not write_yaml.parent.exists():
        logger.error(
            f"YAML file parent ({write_yaml.parent.as_posix()}) doesn't exist."
        )
        raise YAMLError(
            f"YAML file parent ({write_yaml.parent.as_posix()}) doesn't exist."
        )

    logger.info(f"Writing {write_yaml.as_posix()}")
    yaml = YAML()
    with open(write_yaml, "w+") as fp:
        yaml.dump(content, fp)


def write_files(file_path: str | Path, content: str) -> None:
    write_file = Path(file_path) if isinstance(file_path, str) else file_path
    if not write_file.parent.exists():
        write_file.parent.mkdir(parents=True)
    logger.info(f"Writing {write_file.as_posix()}")
    with open(write_file, "w+") as fp:
        fp.write(content)


def get_hash(path: str) -> str:
    BUF_SIZE = 65536
    sha_hash = hashlib.sha256()
    with open(Path(path), "rb") as f:
        while True:
            file = f.read(BUF_SIZE)
            if not file:
                break
            sha_hash.update(file)
    return sha_hash.hexdigest()
