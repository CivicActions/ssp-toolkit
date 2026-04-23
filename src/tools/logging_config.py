"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

load_dotenv()


def _find_project_root(
    start: Path, marker_files: tuple[str, ...] = ("pyproject.toml", ".git")
) -> Path:
    current = start.resolve()
    for parent in (current, *current.parents):
        if any((parent / name).exists() for name in marker_files):
            return parent
    # Fallback: assume .../src/tools/<this_file> and root is 3 levels up
    return start.resolve().parents[2]


def setup_logging() -> None:
    """
    Adds:
      - <root>/auditlogs/audit.log
      - <root>/error.log
    """
    root = _find_project_root(Path(__file__).parent)
    project_path = os.getenv("PROJECT_PATH")
    audit_dir = Path(project_path) / "auditlogs" if project_path else root / "auditlogs"
    audit_dir.mkdir(parents=True, exist_ok=True)

    audit_path = audit_dir / "audit.log"
    error_path = root / "error.log"

    logger.remove()

    # Audit sink (everything, adjust level if you want less noise)
    logger.add(
        str(audit_path),
        level="INFO",
        enqueue=True,
        backtrace=True,
        diagnose=False,
    )

    # Error sink (errors and above only)
    logger.add(
        str(error_path),
        level="ERROR",
        enqueue=True,
        backtrace=True,
        diagnose=True,
        rotation="5 MB",
    )
