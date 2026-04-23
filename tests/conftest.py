"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import pytest

OPENCONTROL_YAML = """\
schema_version: "1.0.0"
name: Test Project
metadata:
  description: Test SSP Project
  maintainers:
    - Test User
components:
  - ./components/TestComponent
standards:
  - ./standards/nist-800-53.yaml
certifications:
  - ./certifications/fisma-low.yaml
"""

CONFIGURATION_YAML = """\
system_security_plan:
  title: Test System Security Plan
  date: "2024-01-01"
certification:
  name: FISMA Low Impact
  abbr: fisma-low
"""

STANDARD_YAML = """\
name: NIST SP 800-53 Rev 5
source: https://csrc.nist.gov/
license: CC0
AC:
  family: Access Control
  name: ACCESS CONTROL
  description: ''
AC-1:
  family: Access Control
  name: Policy and Procedures
  description: >-
    Develop, document, and disseminate access control policy.
AC-2:
  family: Access Control
  name: Account Management
  description: >-
    Manage information system accounts.
"""

CERTIFICATION_YAML = """\
name: FISMA Low Impact
standards:
  NIST SP 800-53 Rev 5:
    AC-1: {}
    AC-2: {}
"""

COMPONENT_YAML = """\
schema_version: "3.1.0"
name: TestComponent
satisfies:
  - control_key: AC-1
    standard_key: NIST SP 800-53 Rev 5
    narrative:
      - key: a
        text: We implement access control policy.
    implementation_statuses:
      - complete
"""


@pytest.fixture()
def project_dir(tmp_path):
    """Create a minimal project directory structure."""
    (tmp_path / "components" / "TestComponent").mkdir(parents=True)
    (tmp_path / "standards").mkdir()
    (tmp_path / "certifications").mkdir()
    (tmp_path / "keys").mkdir()

    (tmp_path / "opencontrol.yaml").write_text(OPENCONTROL_YAML)
    (tmp_path / "configuration.yaml").write_text(CONFIGURATION_YAML)
    (tmp_path / "standards" / "nist-800-53.yaml").write_text(STANDARD_YAML)
    (tmp_path / "certifications" / "fisma-low.yaml").write_text(CERTIFICATION_YAML)
    (tmp_path / "components" / "TestComponent" / "component.yaml").write_text(
        COMPONENT_YAML
    )

    return tmp_path


@pytest.fixture()
def project_env(project_dir, monkeypatch):
    """Set PROJECT_PATH env var to the test project directory."""
    monkeypatch.setenv("PROJECT_PATH", str(project_dir))
    # Clear lru_cache on cached_file_loader so tests don't share state
    try:
        from tools.helpers.helpers import cached_file_loader

        cached_file_loader.cache_clear()
    except Exception:
        pass
    return project_dir
