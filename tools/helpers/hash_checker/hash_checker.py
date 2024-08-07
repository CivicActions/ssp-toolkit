import hashlib
import json
from collections import defaultdict
from pathlib import Path

BUF_SIZE = 65536


class FileChecker:
    hashes: dict[str, str] = defaultdict(lambda: "")
    sha_hash = hashlib.sha256()
    hash_file: Path = Path("file_hashes").with_suffix(".json")
    changed_files: int = 0

    def __init__(self):
        if not Path(self.hash_file).exists():
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
        print(f"Updating file hashes in {self.hash_file.as_posix()}")
        with open(self.hash_file, "w+", encoding="utf-8") as f:
            json.dump(self.hashes, f, indent=2)
