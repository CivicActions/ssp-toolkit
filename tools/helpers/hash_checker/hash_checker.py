import hashlib
import json
from collections import defaultdict
from pathlib import Path

BUF_SIZE = 65536


class FileChecker:
    hashes: dict[str, str] = defaultdict(lambda: "")
    sha_hash = hashlib.sha256()

    def __init__(self):
        if Path("file_hashes.json").exists():
            with open("file_hashes.json", "w+") as f:
                self.hashes = json.dumps(f)

    def get_hash(self, path: str) -> str:
        with open(Path(path), "rb") as f:
            while True:
                file = f.read(BUF_SIZE)
                if not file:
                    break
                self.sha_hash.update(file)
        return self.sha_hash.hexdigest()

    def has_changed(self, path: str) -> bool:
        if not self.hashes or path not in self.hashes:
            self.hashes[path] = self.get_hash(path)
            has_changed = True
        else:
            has_changed = self.hashes[path] != self.get_hash(path)
        return has_changed

    def write_changes(self) -> None:
        with open("file_hashes.json", "w+") as f:
            json.dump(self.hashes, f, indent=2)
