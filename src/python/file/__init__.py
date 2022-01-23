"""
__init__.py - The top-level Python module for the `file` package.
"""
from typing import List

from .base import BaseFile
from .csv import CSVFile
from .text import TextFile


# =========================================================================== #
# METADATA
# =========================================================================== #


__author__ = 'Robert (Bob) L. Jones'
__credits__ = ['Robert (Bob) L. Jones']

__created_date__ = 'Jan 16, 2022'
__modified_date__ = 'Jan 23, 2022'


# =========================================================================== #
# EXPORTS
# =========================================================================== #


__all__: List[str] = [
    'BaseFile',
    'CSVFile',
    'TextFile',
]
