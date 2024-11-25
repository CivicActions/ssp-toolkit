"""
Copyright 2019-2024 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#copyright.
"""

import csv
from collections import OrderedDict
from pathlib import Path
from typing import Optional

from tools.helpers import ssptoolkit


def set_status(existing_status: str = "", component_status: str = "") -> Optional[str]:
    """
    Determine the status of a given control. If there isn't an existing status, set the status
    to the component_status. If one component has the status of "planned" set the status to
    "planned", if a component has the status of "partial", but none are "planned", set the status
    to "partial". If a component has the status of "complete" and no other component has the status
    of either "planned" or "partial" set the status to "complete".

    :param existing_status: a string representing the currently set status.
    :param component_status: a string representing the status for the component that we are checking.
    :return: str
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


def create_rows(controls: dict, header: list) -> list:
    baseline = ssptoolkit.get_certification_baseline()
    empty_row: OrderedDict = OrderedDict.fromkeys(header)
    rows: list = []
    for cid in baseline:
        control_id = cid
        row_data: OrderedDict = (
            controls.get(control_id, OrderedDict())
            if control_id in controls
            else empty_row.copy()
        )
        row: dict = row_data
        row["Control"] = control_id
        rows.append(row)

    return rows


# def get_status(control_id: str) -> str:
#


def get_component_data(
    control_id: str, control: dict, statuses: dict, header: list
) -> dict:
    row: dict = OrderedDict.fromkeys(header)
    row["Control"] = control_id
    row["Status"] = None
    for component in control:
        for key, satisfies in component.items():
            control_key = satisfies.get("control_key")
            status = statuses.get(control_key)
            if not status:
                existing_status = row["Status"]
                component_status = satisfies.get("implementation_status", None)
                status = set_status(
                    component_status=component_status,
                    existing_status=existing_status,
                )
            row["Status"] = status

            row[key] = satisfies.get("security_control_type", None)
    return row


def sort_data(components: dict, header: list) -> dict:
    controls: dict = OrderedDict()
    statuses = ssptoolkit.get_control_statuses()
    for cid, control in components.items():
        row = get_component_data(
            control_id=cid, control=control, statuses=statuses, header=header
        )
        controls[cid] = row
    return controls


def write_file(rows: list):
    output_to = Path("docs")
    if not output_to.is_dir():
        output_to.mkdir()

    matrix = output_to.joinpath("responsibility_matrix.csv")
    print(f"Writing file to {matrix}")
    header = list(rows[0])
    with matrix.open("w+") as fp:
        writer = csv.DictWriter(fp, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)
    print("Write complete")


def main():
    project = ssptoolkit.get_project()
    components = project.get_components()
    header: list = ["Control", "Status"] + [Path(c).name for c in components]
    component_data = ssptoolkit.load_controls_by_id(component_list=components)

    controls = sort_data(components=component_data, header=header)
    rows = create_rows(controls=controls, header=header)
    write_file(rows=rows)


if __name__ == "__main__":
    main()
