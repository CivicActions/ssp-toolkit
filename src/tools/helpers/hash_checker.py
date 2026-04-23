"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import hashlib
import json
from collections import defaultdict
from pathlib import Path

from loguru import logger

from tools.helpers.helpers import get_project_path
from tools.logging_config import setup_logging  # noqa: F401

BUF_SIZE = 65536


class FileChecker:
    hashes: dict[str, str] = defaultdict(lambda: "")
    sha_hash = hashlib.sha256()
    changed_files: int = 0

    def __init__(self) -> None:
        project_path = get_project_path()
        self.hash_file: Path = project_path / "file_hashes.json"
        if not self.hash_file.exists():
            Path(self.hash_file).touch()
        with open(self.hash_file, "r+", encoding="utf-8") as f:
            try:
                self.hashes = json.load(f)
            except json.JSONDecodeError:
                self.hashes = {}

    # Get the file hash for a given file.
    def get_hash(self, path: str) -> str:
        with open(Path(path), "rb") as f:
            while True:
                file = f.read(BUF_SIZE)
                if not file:
                    break
                self.sha_hash.update(file)
        return self.sha_hash.hexdigest()

    # Check if the file has changed.
    def has_changed(self, path: str) -> bool:
        hashed_file = self.get_hash(path)
        if self.hashes.get(path, False):
            has_changed = self.hashes.get(path, "") != hashed_file
        else:
            has_changed = True
        if has_changed:
            self.changed_files += 1
            self.hashes[path] = hashed_file
        return has_changed

    # Write the hashes to the hash_file.json
    def write_changes(self) -> None:
        with open(self.hash_file, "w+", encoding="utf-8") as f:
            json.dump(self.hashes, f, indent=2)
        logger.info(f"Updating file hashes in {self.hash_file.as_posix()}")
        print(f"Updating file hashes in {self.hash_file.as_posix()}")
