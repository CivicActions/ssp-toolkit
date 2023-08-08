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
        return f"{self.party}\n\r{self.narrative}\n\r"


class Control(BaseModel):
    control_id: str
    control_name: str
    description: str
    control_type: str
    status: str
    parts: Dict[str, List[Part]]

    def header(self) -> str:
        return f"## {self.control_id}: {self.control_name}\n\r"

    def control_description(self) -> str:
        return f"```text\n\r{self.description}```\n\r"

    def get_status(self) -> str:
        return f"**Status:** {self.status}\n\r"

    def add_part(self, pid: str, part: Part):
        if pid not in self.parts:
            self.parts[pid] = []
        self.parts[pid].append(part)

    def get_parts(self):
        parts: str = ""
        self.parts = sort_by_keys(self.parts)
        for key, part in self.parts.items():
            for p in part:
                part_key = "" if key == "_default" else key
                parts = parts + f"{part_key}\n\r{str(p)}\n\r"
        return parts

    def __str__(self):
        return f"{self.header()}{self.control_description()}{self.get_status()}{self.get_parts()}"


class Family(BaseModel):
    title: str
    family_id: str
    family_name: str
    controls: Dict[str, Control]

    def header(self):
        return f"# {self.title}\n\r## {self.family_id}: {self.family_name}\n\r"

    def add_control(self, cid: str, control: Control):
        self.controls[cid] = control

    def get_controls(self) -> str:
        text: str = ""
        for key, control in self.controls.items():
            text = text + str(control)
        return text

    def print_family_file(self, out_path: str):
        self.controls = sort_by_keys(self.controls)
        content = self.header() + self.get_controls()
        output = Path(out_path).joinpath(self.family_id).with_suffix(".md")
        with open(output, "w+") as ofp:
            ofp.write(content)

        print(f"writing file {output.as_posix()}")
