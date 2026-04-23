"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/ssp-toolkit#license.
"""

import click
from loguru import logger

from tools.config import check_config
from tools.create_files import create_files_cmd
from tools.create_matrix import create_matrix_cmd
from tools.create_project import create_project_cmd
from tools.export_to import export_to_cmd
from tools.load_project import load_project_cmd
from tools.logging_config import setup_logging
from tools.make_families import make_families_cmd
from tools.make_ssp import make_ssp_cmd
from tools.sop import sop_cmd

setup_logging()


@click.group()
def cli():
    """Command Line Interface for SSP Toolkit"""
    logger.info("CLI started")
    pass


cli.add_command(create_project_cmd)
cli.add_command(load_project_cmd)
cli.add_command(create_files_cmd)
cli.add_command(create_matrix_cmd)
cli.add_command(export_to_cmd)
cli.add_command(make_families_cmd)
cli.add_command(make_ssp_cmd)
cli.add_command(sop_cmd)
cli.add_command(check_config)


if __name__ == "__main__":
    cli()
