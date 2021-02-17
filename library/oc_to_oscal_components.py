from itertools import groupby
from pathlib import Path

import click

from complianceio import opencontrol
from complianceio.oscal import component
from complianceio.oscal.oscal import Metadata
from complianceio.oscal.oscal import oscalize_control_id


@click.command()
@click.argument(
    "source",
    type=click.Path(exists=True, dir_okay=False, file_okay=True, resolve_path=True),
)
def main(source):
    """
    Read an OpenControl repo and emit an OSCAL component definition in JSON.
    """
    p = Path(source)
    oc = opencontrol.load(p)

    md = Metadata(title=oc.name, version="unknown")
    cd = component.ComponentDefinition(metadata=md)
    for o_comp in oc.components:
        c = component.Component(title=o_comp.name, description=o_comp.name)
        c.control_implementations = []

        sorted_controls = sorted(o_comp.satisfies, key=lambda c: c.standard_key)
        grouped_controls = groupby(sorted_controls, lambda c: c.standard_key)
        for standard_key, o_controls in grouped_controls:
            ci = component.ControlImplementation(
                description=standard_key, source=standard_key
            )
            ci.implemented_requirements = []

            for o_control in o_controls:
                control_id = oscalize_control_id(o_control.control_key)
                ir = component.ImplementedRequirement(
                    control_id=control_id, description=f"{control_id} statements"
                )
                for o_statement in o_control.narrative:
                    if o_statement.key:
                        statement_id = f"{control_id}_smt.{o_statement.key}"
                    else:
                        statement_id = f"{control_id}_smt"
                    ir.add_statement(
                        component.Statement(
                            statement_id=statement_id,
                            description=o_statement.text.strip(),
                        )
                    )
                ci.implemented_requirements.append(ir)
            c.control_implementations.append(ci)
        cd.add_component(c)
    root = component.Model(component_definition=cd)
    print(root.json(indent=2))


if __name__ == "__main__":
    main()
