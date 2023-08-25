from complianceio.opencontrol import OpenControl

from tools.helpers import ssptoolkit


def test_sortable_control_id():
    test_cid = ssptoolkit.sortable_control_id("AC-1")
    test_cid_extended = ssptoolkit.sortable_control_id("AC-3 (9)")

    assert test_cid == "AC-01"
    assert test_cid_extended == "AC-03 (09)"


def test_to_oc_control_id():
    oc_simple = ssptoolkit.to_oc_control_id("AC-01")
    oc_extended = ssptoolkit.to_oc_control_id("AC-02 (02)")
    assert oc_simple == "AC-1"
    assert oc_extended == "AC-2 (2)"


def test_get_project():
    project = ssptoolkit.get_project()
    assert isinstance(project, OpenControl)


def test_get_standards():
    title, standards = ssptoolkit.get_standards()
    assert title == "Reusable OpenControl Components (SSP-Toolkit)."
    assert standards[0].get("name") == "NIST SP 800-53 Revision 5"


def test_get_certification_baseline():
    baseline = ssptoolkit.get_certification_baseline()
    assert len(baseline) == 147


def test_get_standards_control_data():
    _, standards = ssptoolkit.get_standards()
    control_data = ssptoolkit.get_standards_control_data(
        control="AC-2", standards=standards
    )
    assert control_data.get("description").find(
        "a. Identifies and selects the following"
    )


def test_get_standards_family_name():
    _, standards = ssptoolkit.get_standards()
    ac = ssptoolkit.get_standards_family_name("AC", standards)
    assert ac == "Access Control"


def test_get_component_files():
    project = ssptoolkit.get_project()
    components = ssptoolkit.get_component_files(project.get_components())
    assert len(components) == 17
    assert "SA-SYSTEM_AND_SERVICES_ACQUISITION" in components


def test_load_controls_by_id():
    project = ssptoolkit.get_project()
    controls = ssptoolkit.load_controls_by_id(project.get_components())
    assert "AC-01" in controls
