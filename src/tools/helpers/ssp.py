"""
Copyright 2019-2026 CivicActions, Inc. See the README file at the top-level
directory of this distribution and at https://github.com/CivicActions/compliancetools#license.
"""

from typing import List

from pydantic import BaseModel

from tools.helpers.family import Family


class Ssp(BaseModel):
    name: str
    standards: List[str]
    families: List[Family]
