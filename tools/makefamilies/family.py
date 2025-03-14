"""
Copyright 2019-2024 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

from collections import OrderedDict
from pathlib import Path
from typing import Dict, List

from pydantic import BaseModel


def sort_by_keys(to_sort: dict) -> OrderedDict:
    return OrderedDict(sorted(to_sort.items()))


class Part(BaseModel):
    key: str
    party: str
    narrative: str

    def __str__(self):
        return f"##### {self.party}\n\n{self.narrative}\n"


class Control(BaseModel):
    control_id: str
    control_name: str
    description: str
    control_type: str | None
    status: str | None
    parts: Dict[str, List[Part]]

    def header(self) -> str:
        return f"### {self.control_id}: {self.control_name}\n\n"

    def control_description(self) -> str:
        return f"```text\n{self.description}\n```\n"

    def get_status(self) -> str:
        return f"**Status:** {self.status}\n"

    def add_part(self, pid: str, part: Part):
        if pid not in self.parts:
            self.parts[pid] = []
        self.parts[pid].append(part)

    def get_parts(self):
        self.parts = sort_by_keys(self.parts)
        parts = ""
        for key, part in self.parts.items():
            part_key = "" if key == "_default" else f"#### {key}"
            parts = parts + part_key
            for p in part:
                parts = parts + f"\n\n{p.__str__()}\n\n"
        return parts

    def __str__(self):
        return f"{self.header()}{self.control_description()}{self.get_status()}{self.get_parts()}"


class Family(BaseModel):
    title: str
    family_id: str
    family_name: str
    controls: Dict[str, Control]

    def header(self):
        return f"# {self.title}\n\n## {self.family_id}: {self.family_name}\n\n"

    def add_control(self, cid: str, control: Control):
        self.controls[cid] = control

    def get_controls(self) -> str:
        text: str = ""
        for key, control in self.controls.items():
            text = text + str(control)
        return text

    def print_family_file(self, out_path: str | Path):
        self.controls = sort_by_keys(self.controls)
        content = self.header() + self.get_controls()
        output = Path(out_path).joinpath(self.family_id).with_suffix(".md")
        with open(output, "w+") as ofp:
            ofp.write(content)

        print(f"writing file {output.as_posix()}")
