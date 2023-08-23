# Copyright 2019-2020 CivicActions, Inc. See the README file at the top-level
# directory of this distribution and at https://github.com/CivicActions/compliancetools#copyright.

import csv
from collections import OrderedDict
from pathlib import Path
from typing import Optional

import yaml

from tools.lib import ssptoolkit


def set_status(existing_status: str = "", component_status: str = "") -> Optional[str]:
    """
    Create matri
    """
    new_status = None
    if not existing_status and component_status:
        new_status = component_status
    elif component_status:
        if component_status.lower() == "planned":
            new_status = component_status
        elif (
            component_status.lower() == "partial"
            and existing_status.lower() != "planned"
        ):
            new_status = component_status
        elif component_status.lower() == "complete" and existing_status.lower() not in [
            "planned",
            "partial",
        ]:
            new_status = component_status
        else:
            new_status = component_status
    return new_status


def sort_data(components: dict, header: list):
    try:
        with open("keys/status.yaml", "r") as fp:
            statuses = yaml.load(fp, Loader=yaml.SafeLoader)
    except FileNotFoundError as error:
        raise error

    rows: list = []
    for cid, control in components.items():
        row: dict = OrderedDict.fromkeys(header)
        row["Control"] = cid
        row["Status"] = None
        for component in control:
            for key, satisfies in component.items():
                status = statuses.get(satisfies.get("control_key"))
                if not status:
                    existing_status = row["Status"]
                    component_status = satisfies.get("implementation_status", None)
                    status = set_status(
                        component_status=component_status,
                        existing_status=existing_status,
                    )
                row["Status"] = status

                row[key] = satisfies.get("security_control_type", None)
        rows.append(row)

    write_file(rows=rows)


def write_file(rows: list):
    output_to = Path("docs")
    if not output_to.is_dir():
        output_to.mkdir()

    matrix = output_to.joinpath("responsibility_matrix.csv")
    print(f"Writing file to {matrix}")
    header = list(rows[0])
    with open(matrix, "w+") as fp:
        writer = csv.DictWriter(fp, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)
    print("Write complete")


def main():
    """
    creatematrix creates a Responsibility Matrix spreadsheet show
    """
    project = ssptoolkit.load_project_data()
    components = project.get_components()
    header: list = ["Control", "Status"] + [Path(c).name for c in components]
    component_data = ssptoolkit.load_controls_by_id(component_list=components)

    sort_data(components=component_data, header=header)


if __name__ == "__main__":
    main()
